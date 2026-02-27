from django.urls import path
from api.views import categories_list

app_name = 'api'

urlpatterns = [
    path('categories/', categories_list, name='categories'),
]