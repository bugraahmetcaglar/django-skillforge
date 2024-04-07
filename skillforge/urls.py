"""
URL configuration for skillforge project.
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# For new version path example:
# re_path(r'^users/(?P<user_uuid>[0-9a-f-]{32})/$', user_detail_view, name='user_detail'),


schema_view = get_schema_view(
    openapi.Info(
        title="Skillforge API Swagger",
        default_version="v2",
        description="Skillforge Swagger",
        terms_of_service="",
        contact=openapi.Contact(email="bugraahmetcaglar@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

v1_urls = [
    path("admin/", admin.site.urls),
    path("v1/user/", include("core.user.v1.urls")),
]

v2_urls = [
    path("v2/user/", include("core.user.v1.urls")),
]

# Documentation
swagger_urls = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns = v1_urls + v2_urls + swagger_urls
