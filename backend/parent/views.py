from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from .models import Task, parent
from .serializers import CreateUserSerializer, TaskSer


class createParent(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        instnce = parent.objects.create(
            user=request.user, student=request.data['student'])
        return Response(status=status.HTTP_200_OK)


class TaskView():
    def post(self, request, format=None):
        data = request.data
        title = data['title']
        desc = data['desc']
        start = data['start']
        end = data['end']
        reward = data['reward']
        parent = request.user
        parentinstance = parent.objects.get(user=parent).first()
        student = parentinstance.student
        instance = Task.objects.create(
            student=student,
            title=title,
            desc=desc,
            start=start,
            end=end,
            reward=reward,)
        instance.save()
        return Response(data={"msg": "ok created"}, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        parent = request.user
        parentinstance = parent.objects.get(user=parent).first()
        student = parentinstance.student
        instance = Task.objects.filter(student=student)
        serializer = TaskSer(instance, many=True)
        return Response(serializer.data)


class TaskStudentView(APIView):
    def get(self, request):
        student = request.user
        instance = Task.objects.filter(student=student)
        serinstance = TaskSer(instance, many=True)
        return Response(serinstance.data)


class TaskInstanceView(APIView):
    def get(self, request, pk, format=None):
        instance = Task.objects.get(id=pk)
        serializer = TaskSer(instance)
        return Response(serializer.data)


class TaskActionView(APIView):
    def put(self, request):
        data = request.data
        id = data['id']
        instance = Task.objects.get(id=id)
        instance.status = True
        instance.save()
        return Response(data={"msg": "ok"}, status=status.HTTP_200_OK)
