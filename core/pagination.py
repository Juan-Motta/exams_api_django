from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page = 1
    page_size = 20
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "current_page": int(self.request.GET.get("page", 1)),
                "data": data,
                "last_page_url": self.get_previous_link(),
                "next_page_url": self.get_next_link(),
                "to": int(self.request.GET.get("page_size", self.page_size)),
                "total": self.page.paginator.count,
            },
        )
