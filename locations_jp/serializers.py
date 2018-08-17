from django.db.models import Model
from rest_framework import serializers, fields
from . import models


class JpAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.JpAddress
        fields = '__all__'


class PrefectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Prefecture
        fields = ['id', 'code', 'slug', 'name', 'kana', 'region', 'neighbors']
