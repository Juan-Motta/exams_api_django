from apps.users.views import UserCreateAndRetrieveApiView

from django.urls import path

urlpatterns = [
    path(route='', view=UserCreateAndRetrieveApiView.as_view(), name='users_create_and_retrieve'),
]
