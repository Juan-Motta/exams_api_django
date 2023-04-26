from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns_v1 = [
    path("api/admin", admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/schema/swagger',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/schema/redoc',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    path(
        "api/v1/users",
        include(("apps.users.urls", "users"), namespace="users"),
    ),
]

urlpatterns = urlpatterns_v1
