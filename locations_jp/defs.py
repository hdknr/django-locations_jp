from django.db import models
from django.utils.translation import ugettext_lazy as _


class Region(models.Model):
    code = models.CharField(max_length=10, db_index=True, unique=True,)
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Prefecture(models.Model):
    code = models.CharField(max_length=10, db_index=True, unique=True,)
    slug = models.CharField(max_length=50, db_index=True, unique=True,)
    name = models.CharField(max_length=50, db_index=True, unique=True,)
    kana = models.CharField(max_length=50, db_index=True)
    shortname = models.CharField(max_length=50)
    jpaddress_url = models.URLField(null=True, blank=True, default=None)

    class Meta:
        abstract = True


class City(models.Model):
    jiscode = models.CharField(_('JIS X0401/X0402'), max_length=10)
    name = models.CharField(max_length=150)
    kana = models.CharField(max_length=100)

    class Meta:
        abstract = True


class JpAddress(models.Model):
    jiscode = models.CharField(_('JIS X0401/X0402'), max_length=10)
    zipcode5 = models.CharField(max_length=5)
    zipcode = models.CharField(max_length=7)

    pref_kana = models.CharField(max_length=50)
    city_kana = models.CharField(max_length=100)
    town_kana = models.CharField(max_length=100)

    pref_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=150)
    town_name = models.CharField(max_length=150)

    is_split = models.BooleanField()
    is_small = models.BooleanField()
    is_towncode = models.BooleanField()
    is_multi  = models.BooleanField()
    is_changed  = models.IntegerField()
    ''' 0 = no changed , 1 = changed , 2 = discontinued '''
    reason   = models.IntegerField()
    ''' 0: unchange, 1: administrative reason,
        2: residential, 3: land readjustment,
        4: postal, 5: correction, 7: discontinued
    '''

    class Meta:
        abstract = True
