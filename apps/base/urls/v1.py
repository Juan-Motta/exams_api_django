from apps.base.views.country import CountryAPIView

from django.urls import path

urlpatterns = [
    path(route='/country', view=CountryAPIView.as_view(), name='country'),
]
