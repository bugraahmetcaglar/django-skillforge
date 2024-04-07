from django.db import models

from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


import logging

logger = logging.getLogger(__name__)


class NullableCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        max_length = kwargs.pop("max_length", 254)
        default = kwargs.pop("default", None)
        super().__init__(max_length=max_length, default=default, null=True, *args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["null"]
        return name, path, args, kwargs


class BaseResponse:
    def __init__(self, status_code=status.HTTP_200_OK, message="", data=None):
        self.status_code = status_code
        self.message = message
        self.data = data

    def success(self):
        return Response({"success": True, "message": self.message}, self.status_code)

    def error(self):
        return Response({"success": False, "message": self.message}, self.status_code)

    def success_data(self):
        return Response({"success": True, "data": self.data}, self.status_code)
    

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 1000
