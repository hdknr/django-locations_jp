from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views, viewsets

router = DefaultRouter()
router.register(r'jpaddress', viewsets.JpAddressViewSet, base_name='jpaddress')

urlpatterns = [
    url(r'^', include(router.urls)),
]
