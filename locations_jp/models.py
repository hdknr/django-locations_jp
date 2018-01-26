from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import defs


class Region(defs.Region):

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')
        ordering = ['code']

    def __str__(self):
        return self.name


class Prefecture(defs.Prefecture):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    neighbors = models.ManyToManyField('self', blank=True)

    class Meta:
        verbose_name = _('Prefecture')
        verbose_name_plural = _('Prefectures')
        ordering = ['code']

    def __str__(self):
        return self.name


class City(defs.City):
    prefecture = models.ForeignKey(
        Prefecture, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('City')

    def __str__(self):
        return " ".join([str(self.prefecture), self.name])


class JpAddress(defs.JpAddress):
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        verbose_name = _('JP Address')
        verbose_name_plural = _('JP Address')

    def __str__(self):
        return ' '.join([self.zipcode, str(self.city)])
