from django.db import models, connection
from django.template import Template, Context, loader
try:
    from django.urls import reverse
except:
    from django.core.urlresolvers import reverse
import requests
import zipfile
import io


def admin_change_url_name(model):
    return 'admin:{0}_{1}_change'.format(
            model._meta.app_label, model._meta.model_name, )


def admin_change_url(instance):
    return reverse(admin_change_url_name(instance), args=[instance.id])


def render(src, request=None, **kwargs):
    return Template(src).render(Context(kwargs))


def render_by(name, request=None, **kwargs):
    return loader.get_template(name).render(context=kwargs)


def call_sql(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    more = True
    res = []
    while more:
        res.append(cursor.fetchall())
        more = cursor.nextset()
    cursor.close()
    return res

def open_zipfile(url):
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as thezip:
        for zipinfo in thezip.infolist():
            with thezip.open(zipinfo) as thefile:
                thefile = io.TextIOWrapper(
                    io.BytesIO(thefile.read()), encoding='cp932')
                yield zipinfo.filename, thefile
