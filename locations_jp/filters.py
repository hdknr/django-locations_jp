'''
https://django-filter.readthedocs.io/en/master/
- Depreciation 2.0: https://github.com/carltongibson/django-filter/pull/792
'''

import django_filters
from . import models


class JpAddressFilter(django_filters.FilterSet):
    zc = django_filters.CharFilter(field_name='zipcode', lookup_expr='startswith')

    class Meta:
        model = models.JpAddress
        exclude = []


class PrefectureFilter(django_filters.FilterSet):

    class Meta:
        model = models.Prefecture
        exclude = []