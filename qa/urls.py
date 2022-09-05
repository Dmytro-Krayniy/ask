from django.urls import url
from .views import test

urlpatterns = [
    url(r'^$', test),
    url(r'^<\d+>/$', test),
]
