from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('new/', new, name='new'),
    path('', new, name='home'),
    path('<int:q_id>/', question_details, name='question_details'),
#    path('scrap/', scrap),
    path('popular/', popular, name='popular'),
    path('ask/', ask, name='ask')
]

