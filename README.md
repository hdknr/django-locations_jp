# django-locations_jp

- Prefectures
- City
- JP Address

## Load Prefectures

~~~bash
$ python manage.py locations_jp load_prefecture fixtures/prefectures.json
.
~~~

## Set JP Address URL

~~~bash
$ python manage.py locations_jp jp_urls
.
~~~

## Load JP Address Data

MySQL and All(KEN_ALL):

~~~bash
$ python manage.py locations_jp_mysql import_jpaddress
$ python manage.py locations_jp_mysql process_jpaddress
.
~~~
