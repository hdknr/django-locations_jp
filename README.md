# django-locations_jp(proto)

- Prefectures
- City
- JP Address

## Load Prefectures

~~~bash
$ python manage.py locations_jp_run load_prefecture fixtures/prefectures.json
~~~

## Set JP Address URL

~~~bash
$ python manage.py locations_jp_run jp_urls
~~~

## Load JP Address Data

MySQL and All(KEN_ALL):

~~~bash
$ python manage.py locations_jp_mysql import_jpaddress
$ python manage.py locations_jp_mysql process_jpaddress
~~~
