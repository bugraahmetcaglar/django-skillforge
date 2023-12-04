from django.urls import re_path
from rest_framework_simplejwt.views import TokenRefreshView

from user.v1.api import (
    UserLoginAPIView, UserRegistrationAPIView, UserLogoutAPIView, 
    UserListAPIView, UserDetailAPIView
)


urlpatterns = [
    re_path(r'^user/detail/(?P<id>[\w-]+)$', UserDetailAPIView.as_view(), name='user_detail_api'),
    re_path(r'^user/login$', UserLoginAPIView.as_view(), name="user_login_api"),
    re_path(r'^user/list$', UserListAPIView.as_view(), name="user_list_api"),
    re_path(r'^user/login/refresh$', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^user/register$', UserRegistrationAPIView.as_view(), name='user_create_api'),
    re_path(r'^user/logout$', UserLogoutAPIView.as_view(), name='user_logout_api'),
]
