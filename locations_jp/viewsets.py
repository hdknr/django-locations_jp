from collections import OrderedDict
from rest_framework import (viewsets, permissions, pagination, response, decorators)
from . import models, serializers, filters


class Pagination(pagination.PageNumberPagination):
    page_size = 100
    max_page_size = 100
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return response.Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_range', list(self.page.paginator.page_range)),
            ('current_page', self.page.number),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))

class JpAddressViewSet(viewsets.ModelViewSet):
    queryset = models.JpAddress.objects.all()
    serializer_class = serializers.JpAddressSerializer
    filter_class = filters.JpAddressFilter
    pagination_class = Pagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class PrefectureViewSet(viewsets.ModelViewSet):
    queryset = models.Prefecture.objects.all()
    serializer_class = serializers.PrefectureSerializer
    filter_class = filters.PrefectureFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    @decorators.action(methods=['get'], detail=False)
    def names(self, request):
        items = models.Prefecture.objects.values_list('name', flat=True)
        return response.Response(items) 