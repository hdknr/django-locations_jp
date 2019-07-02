from django import template
from django.contrib.staticfiles import finders
from locations_jp import models, api, utils

register = template.Library()


@register.simple_tag
def prefectures():
    return utils.to_json(
        api.serializers.PrefectureSerializer(
            models.Prefecture.objects.all(), many=True).data)
