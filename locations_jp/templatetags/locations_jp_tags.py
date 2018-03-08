from django import template
from django.contrib.staticfiles import finders
from locations_jp import models, serializers, utils

register = template.Library()


@register.simple_tag
def prefectures():
    return utils.to_json(
        serializers.PrefectureSerializer(
            models.Prefecture.objects.all(), many=True).data)
