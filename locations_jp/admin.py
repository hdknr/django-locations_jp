from django.contrib import admin
from ordered_model.admin import OrderedTabularInline, OrderedModelAdmin
from . import models, utils


class Mixin(object):
    def admin_url(self, obj):
        return utils.render('''<a href="{{u}}">{{i}}</a>''',
            u=utils.admin_change_url(obj), i=obj)


class PrefectureInline(admin.TabularInline, Mixin):
    model = models.Prefecture
    extra = 0
    fields = ['admin_url']
    readonly_fields = ['admin_url']

@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name', ]
    inlines = [PrefectureInline]


class CityInline(admin.TabularInline, Mixin):
    model = models.City
    extra = 0
    fields = ['admin_url']
    readonly_fields = ['admin_url']


@admin.register(models.Prefecture)
class PrefectureAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name', 'kana']
    list_filter = ['region']
    inlines = [CityInline]


class JpAddressInline(admin.TabularInline, Mixin):
    model = models.JpAddress
    extra = 0
    fields = ['admin_url', 'town_name', 'town_kana', ]
    readonly_fields = ['admin_url', 'zipcode', 'town_name', 'town_kana', ]


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'jiscode', 'prefecture', 'name', 'kana']
    raw_id_fields = ['prefecture']
    list_filter = ['prefecture']
    inlines = [JpAddressInline]
    search_fields = ['name', 'kana', 'prefecture__name', 'prefecture__kana']


@admin.register(models.JpAddress)
class JpAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'jiscode', 'zipcode',
                    'pref_name', 'city_name', 'town_name']
    raw_id_fields = ['city']
    list_filter = [
        'pref_name',
        'is_split', 'is_small', 'is_towncode',
        'is_multi', 'is_changed', 'reason', ]
    search_fields = ['pref_name', 'city_name', 'town_name',
                     'pref_kana', 'city_kana', 'town_kana', ]
