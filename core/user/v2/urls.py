from django.urls import re_path
from rest_framework_simplejwt.views import TokenRefreshView

from core.user.v2.views import (
    UserLoginAPIView,
    UserRegistrationAPIView,
    UserLogoutAPIView,
    UserListAPIView,
    UserDetailAPIView,
)


urlpatterns = [
    re_path(r"^detail/(?P<id>[\w-]+)$", UserDetailAPIView.as_view(), name="v1_user_detail"),
    re_path(r"^login$", UserLoginAPIView.as_view(), name="v2_user_login"),
    re_path(r"^list$", UserListAPIView.as_view(), name="v1_user_list"),
    re_path(r"^register$", UserRegistrationAPIView.as_view(), name="v1_user_create"),
    re_path(r"^logout$", UserLogoutAPIView.as_view(), name="v1_user_logout"),
    re_path(r"^login/refresh$", TokenRefreshView.as_view(), name="v1_token_refresh"),
]
