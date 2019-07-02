from pyexcel_xlsx import get_data as excel_get_data
import djclick as click
from django.utils import translation
from locations_jp import models, conf, utils
from locations_jp.models import batch
from logging import getLogger
log = getLogger()

translation.activate('ja')


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.option('--url', default=conf.JP_KEN_ALL)
@click.option('--pref')
@click.option('--out')
@click.pass_context
def import_jpaddress(ctx, url, pref, out):
    '''
    CP932=MS932=MS漢字コード=Windows-31J≒Shift JIS
    http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip
    '''
    def _run(pref_url, out):
        for name, file in utils.open_zipfile(pref_url):
            if name.endswith('.CSV'):
                out = out and open(out, 'w')
                dry = out is not None
                batch.mysql_jpaddress_import(file, out=out, dry=dry)
                if not dry:
                    call_batch()

    urls = []
    if pref == 'all':
        urls = [pref.jpaddress_url for pref in models.Prefecture.objects.all() if pref.jpaddress_url]
    else:
        prefecture  = pref and models.Prefecture.objects.filter(name=pref).first()
        if prefecture:
            urls = [prefecture.jpaddress_url or url]
    
    for u in urls:
        _run(u, out)


def call_batch():
    batch.mysql_city_import()
    batch.mysql_city_update()
    batch.mysql_city_insert()
    batch.mysql_jpaddress_insert()


@main.command()
@click.pass_context
def process_jpaddress(ctx):
    ''' '''
    call_batch()
