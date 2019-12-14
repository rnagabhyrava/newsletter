from django.urls import path
from django.conf.urls import url

from . import views
from weather.views import LocationAutocomplete

app_name = "weather"

urlpatterns = [
    path('', views.signup, name='signup'),
    # path('', EmailCreate.as_view(), name='signup'),
    path('done/', views.done, name='done'),
    url(
        r'^location-autocomplete/$',
        LocationAutocomplete.as_view(),
        name='location-autocomplete',
    ),
]