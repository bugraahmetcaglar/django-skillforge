# Bugra Ahmet Caglar
from drf_yasg.utils import swagger_auto_schema

from skillforge.generics import StandardResultsSetPagination
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework_jwt.settings import api_settings

from core.user.models import User
from core.user.v1.serializers import (
    UserLoginSerializer,
    UserRegisterSerializer,
    UserLogoutSerializer,
    UserListSerializer,
)
from skillforge.utils import BaseResponse


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(operation_summary="User login API")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return BaseResponse(data=serializer.data, status_code=status.HTTP_200_OK).success_data()


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(operation_summary="Create a new user API")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return BaseResponse(message="User created successfully.", status_code=status.HTTP_201_CREATED).success()


class UserDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    lookup_field = "id"


class UserLogoutAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserLogoutSerializer

    @swagger_auto_schema(operation_summary="Logout api")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return BaseResponse(message="Successfully logged out.", status_code=status.HTTP_200_OK).success()


class UserListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserListSerializer
    pagination_class = StandardResultsSetPagination
    queryset = User.objects.filter(is_active=True)
    lookup_field = "id"

    def list(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(self.queryset, many=True).data
        return BaseResponse(data=serializer_data, status_code=status.HTTP_200_OK).success_data()
