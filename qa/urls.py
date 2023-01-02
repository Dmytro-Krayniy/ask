from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('new/', new),
    path('', new, name='home'),
    path('<int:q_id>/', question_info),
    path('scrap/', scrap),
    path('popular/', popular),
    path('ask/', ask)
]

