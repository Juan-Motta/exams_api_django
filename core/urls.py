from django.contrib import admin
from django.urls import include, path

urlpatterns_v1 = [
    path("api/admin", admin.site.urls),
    path(
        "api/v1", include(("apps.base.urls.v1", "base"), namespace="base_v1")
    ),
    path(
        "api/v1/users",
        include(("apps.users.urls.v1", "users"), namespace="users_v1"),
    ),
]

urlpatterns = urlpatterns_v1
