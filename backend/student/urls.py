from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *


urlpatterns = [
    path('student/',
         StudentDataView.as_view(),
         name='student view'),
    path('appusage/',
         AppUsageDataView.as_view(),
         name='appusage view'),
    path('audio/',
         StudentAudioView.as_view(),
         name='audio view'),
    path('student/<str:pk>/',
         studentInstanceview.as_view(),
         name='student view'),
    path('appusage/<str:pk>/',
         appUsageInstanceview.as_view(),
         name='appusage view'),
    path('audio/<str:pk>/',
         studentAudioInstanceview.as_view(),
         name='audio view'),
    path('feeling/', Feeling.as_view(), name="feeling"),
    

]
