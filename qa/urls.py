from django.urls import path, re_path
from .views import test

urlpatterns = [
    re_path(r'', test),
    re_path('^<\d+>/$', test),
]
