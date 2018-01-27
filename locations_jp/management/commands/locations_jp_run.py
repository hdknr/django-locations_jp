from pyexcel_xlsx import get_data as excel_get_data
import djclick as click
from django.utils import translation
from locations_jp import models, defs, batch, conf, utils
from logging import getLogger
from bs4 import BeautifulSoup as Soup
from urllib.parse import urljoin
import requests
import json
import csv
import unicodedata
log = getLogger()

translation.activate('ja')


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass

def get_or_create_region(id, name):
    if not all([id, name]):
        return None, None
    return models.Region.objects.get_or_create(code=id, name=name)


def update_or_create_prefecture(
        region, id=None, name=None, short=None, kana=None, en=None):
    slug = en or id
    if not all([region, id, slug, name]):
        return False
    if region.prefecture_set.filter(slug=slug).update(
        code=id, name=name, kana=kana, shortname=short) > 0:
        return region.prefecture_set.filter(slug=slug).first()

    return region.prefecture_set.create(
        slug=slug, code=id, name=name, kana=kana, shortname=short)



@main.command()
@click.argument('path')
@click.pass_context
def load_prefecture(ctx, path):
    data = json.load(open(path))

    for row in data.values():
        area = row.pop('area', {})
        neighbor = row.pop('neighbor', {})
        region, created = get_or_create_region(**area)
        prefecture = update_or_create_prefecture(region, **row)

    data = json.load(open(path))
    for row in data.values():
        neighbor = row.pop('neighbor', {})
        prefecture = models.Prefecture.objects.filter(code=row['id']).first()
        for ndata in neighbor.values():
            nobj = models.Prefecture.objects.filter(code=ndata['id']).first()
            nobj and prefecture.neighbors.add(nobj)


@main.command()
@click.pass_context
def jp_urls(ctx):
    url = 'http://www.post.japanpost.jp/zipcode/dl/kogaki-zip.html'
    soup = Soup(requests.get(url).content, "html.parser")
    for a in soup.select(".arrange-c a"):
        path = a['href']
        if path.endswith(".zip"):
            models.Prefecture.objects.filter(name=a.text).update(
                jpaddress_url=urljoin(url, path))


def get_or_create_city(jiscode, pref_name, city_name, city_kana):
    prefecture = models.Prefecture.objects.filter(name=pref_name).first()
    if not prefecture:
        return
    city, created = prefecture.city_set.get_or_create(
        jiscode=jiscode, name=city_name, kana=city_kana)
    return city


def load_jpaddress_csv(file):
    names = [f.name for f in defs.JpAddressCsv._meta.fields]
    for row in csv.reader(file):
        for i in [3, 4, 5]:
            row[i] = unicodedata.normalize('NFKC', row[i])
        keys = dict(zip(names[:6], row[:6]))
        data = dict(zip(names[6:], row[6:]))
        city = get_or_create_city(
            keys['jiscode'], data['pref_name'],
            data['city_name'], keys['city_kana'])
        if city:
            data['city'] = city

        if models.JpAddress.objects.filter(**keys).update(**data) < 1:
            data.update(keys)
            models.JpAddress.objects.create(**data)


@main.command()
@click.option('--url', default=conf.JP_KEN_ALL)
@click.option('--pref')
@click.pass_context
def load_jpaddress(ctx, url, pref):
    '''
    CP932=MS932=MS漢字コード=Windows-31J≒Shift JIS
    http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip
    '''
    prefecture  = pref and models.Prefecture.objects.filter(name=pref).first()
    if prefecture:
        url = prefecture.jpaddress_url or url

    for name, file in utils.open_zipfile(url):
        if name.endswith('.CSV'):
            load_jpaddress_csv(file)
