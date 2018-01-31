'''
https://django-filter.readthedocs.io/en/master/
'''

import django_filters
from . import models


class JpAddressFilter(django_filters.FilterSet):

    class Meta:
        model = models.JpAddress
        exclude = []
