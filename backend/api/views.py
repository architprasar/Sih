from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from api.serializers import CreateUserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class CreateUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        instance = User.objects.filter(username=data['username']).first()
        if instance:
            return Response({'msg': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(
            username=data['username'],
            email=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        user.set_password(data['password'])
        user.save()

        token = Token.objects.create(user=user)
        token_data = {"token": token.key}
        return Response({**token_data}, status=status.HTTP_201_CREATED,)


class LogoutUserAPIView(APIView):
    queryset = get_user_model().objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class LoginUserAPIView(APIView):
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        print(user)
        return Response(status=status.HTTP_200_OK)


class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        print(request.headers)
        user = authenticate(
            username=data['username'], password=data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(data={"msg": "invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
class ReturnProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        instance = User.objects.filter(username=user).first()
        print(user.username)

        return Response(data={"name": instance.first_name, "last_name": instance.last_name, "email": instance.email}, status=status.HTTP_200_OK)
