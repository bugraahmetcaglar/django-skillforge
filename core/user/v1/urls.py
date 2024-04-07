from django.urls import re_path
from rest_framework_simplejwt.views import TokenRefreshView

from core.user.v1.views import (
    UserLoginAPIView,
    UserRegistrationAPIView,
    UserLogoutAPIView,
    UserListAPIView,
    UserDetailAPIView,
)

urlpatterns = [
    # Example with Regex (old version django)
    re_path(r"^detail/(?P<id>[\w-]+)$", UserDetailAPIView.as_view(), name="user_detail_api"),
    re_path(r"^detail/(?P<id>[\w-]+)$", UserDetailAPIView.as_view(), name="user_detail_api"),
    re_path(r"^login$", UserLoginAPIView.as_view(), name="user_login_api"),
    re_path(r"^list$", UserListAPIView.as_view(), name="user_list_api"),
    re_path(r"^login/refresh$", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r"^register$", UserRegistrationAPIView.as_view(), name="user_create_api"),
    re_path(r"^logout$", UserLogoutAPIView.as_view(), name="user_logout_api"),
]
