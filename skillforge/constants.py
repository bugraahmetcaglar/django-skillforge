from rest_framework import status
from rest_framework.response import Response

import logging

logger = logging.getLogger(__name__)


class BaseResponse:
    def __init__(self, status_code=status.HTTP_200_OK, message="", data=None):
        self.status_code = status_code
        self.message = message
        self.data = data

    def success(self):
        return Response({"success": status.HTTP_201_CREATED, "message": self.message}, self.status_code)

    def error(self):
        return Response(
            {
                "success": False,
                "message": self.message,
            },
            self.status_code,
        )

    def success_with_data(self):
        return Response({"success": self.success, "data": self.data}, self.status_code)
