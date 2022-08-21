from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, Login, LoginUserAPIView, LogoutUserAPIView


urlpatterns = [
    path('auth/login/',
         Login.as_view(),
         name='auth_user_login'),
    path('auth/register/',
         CreateUserAPIView.as_view(),
         name='auth_user_create'),
    path('auth/logout/',
         LogoutUserAPIView.as_view(),
         name='auth_user_logout'),
    path('auth/',
         LoginUserAPIView.as_view(),
         name='auth_user_logout'),

]
