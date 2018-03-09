'''
https://django-filter.readthedocs.io/en/master/
'''

import django_filters
from . import models


class JpAddressFilter(django_filters.FilterSet):
    zc = django_filters.CharFilter(name='zipcode', lookup_expr='startswith')

    class Meta:
        model = models.JpAddress
        exclude = []
