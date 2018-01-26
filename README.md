## django-locations_jp

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

All(KEN_ALL):

~~~bash
$ python manage.py locations_jp_run load_jpaddress
~~~

Specific prefecture:

~~~bash
$ python manage.py locations_jp_run load_jpaddress --pref 沖縄県
~~~
