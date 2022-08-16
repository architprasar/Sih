from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from api.serializers import CreateUserSerializer
from .serializers import *
from .models import *


# Create your views here.

class StudentDataView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        age = data['age']
        address = data['address']
        phone = data['phone']
        user = request.user
        instance  = student.objects.create(age=age, address=address, phone=phone, user=user)


        return Response({"msg":"created"},status=status.HTTP_201_CREATED)
    def get(self, request, format=None):
        instance = student.objects.all()
        serializer = studentser(instance, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class AppUsageDataView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        appName = data['appname']
        appUsage = data['appusage']
        user = request.user
        instance  = appUsageData.objects.create(appName=appName, appUsage=appUsage, user=user)
        return Response( status=status.HTTP_201_CREATED)


    def get(self, request, format=None):
        instance = appUsageData.objects.all()
        serializer = appusagedataser(instance, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class StudentAudioView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        audio = data['audio']
        user = request.user
        instance  = studentAudio.objects.create(audio=audio, user=user)
        return Response( status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        instance = studentAudio.objects.all()
        serializer = studentaudioser(instance, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class studentInstanceview(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request,pk, format=None):
        instance = student.objects.filter(id=pk).first()
        serializer = studentser(instance)
        return Response(serializer.data,status=status.HTTP_200_OK)


class appUsageInstanceview(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request,pk, format=None):
        instance = appUsageData.objects.filter(id=pk).first()
        serializer = appusagedataser(instance)
        return Response(serializer.data,status=status.HTTP_200_OK)

class studentAudioInstanceview(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request,pk, format=None):
        instance = studentAudio.objects.filter(id=pk).first()
        serializer = studentaudioser(instance)
        return Response(serializer.data,status=status.HTTP_200_OK)

