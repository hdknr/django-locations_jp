from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views, viewsets

router = DefaultRouter()
router.register(r'jpaddress', viewsets.JpAddressViewSet, base_name='jpaddress')
router.register(r'prefecture', viewsets.PrefectureViewSet, base_name='prefecture')


urlpatterns = [
    url(r'^', include(router.urls)),
]
