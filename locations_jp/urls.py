from django.urls import path, include


urlpatterns = [
    path('api/', include('locations_jp.api.urls')),
]
