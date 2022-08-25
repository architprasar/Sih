from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *


urlpatterns = [
    path('add/parent/',
         createParent,
         name='create parent'),
    path('add/task/', TaskView, name="add task "),
    path('task/<int:pk>', TaskInstanceView, name="task instance view"),





]
