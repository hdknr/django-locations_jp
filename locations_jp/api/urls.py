from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'jpaddress', viewsets.JpAddressViewSet, base_name='jpaddress')
router.register(r'prefecture', viewsets.PrefectureViewSet, base_name='prefecture')


urlpatterns = [
    path('', include(router.urls)),
]
