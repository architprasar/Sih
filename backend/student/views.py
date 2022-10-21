from datetime import datetime
import json
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from api.serializers import CreateUserSerializer
from .serializers import *
from .models import *
import base64
from django.utils import timezone
from django.core.files.base import ContentFile
from tensorflow import keras
import librosa
import IPython.display as ipd
from keras.models import model_from_json
import numpy as np
import pickle
import pandas as pd
# Create your views here.


class StudentDataView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        age = data['age']
        address = data['address']
        phone = data['phone']
        user = request.user
        instance = student.objects.create(
            age=age, address=address, phone=phone, user=user)

        return Response({"msg": "created"}, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        instance = student.objects.all()
        serializer = studentser(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AppUsageDataView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        appName = data['appname']
        appUsage = data['appusage']
        user = request.user
        instance = appUsageData.objects.create(
            appName=appName, appUsage=appUsage, user=user)
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        instance = appUsageData.objects.all()
        serializer = appusagedataser(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentAudioView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data
        user = request.user
        audio = data['audio']

        user = request.user
        aud = audio.split('base64,')[1]
        name = 'temp'+str(audio[5:10])+'.' + 'wav'
        ta = ContentFile(base64.b64decode(aud),
                         name=name)
        instance = studentAudio.objects.create(
            audio=ta
        )

        json_file = open(
            'C:/Users/91788/Desktop/pro2/backend/media/audio/model_json.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        newData, newSR = librosa.load(
            "media/audio/"+name, duration=2.5, sr=44100, offset=0.5)

        newSR = np.array(newSR)
        mfccs = np.mean(librosa.feature.mfcc(
            y=newData, sr=newSR, n_mfcc=13), axis=0)
        newdf = pd.DataFrame(data=mfccs).T
        newdf = np.expand_dims(newdf, axis=2)

        print(newdf.shape)
        new = loaded_model.predict(newdf)
        print(new)
        filename = 'media/audio/labels'

        infile = open(filename, 'rb')
        lb = pickle.load(infile)
        infile.close()

# Get the final predicted label
        final = new.argmax(axis=1)
        final = final.astype(int).flatten()
        final = (lb.inverse_transform((final)))
        if final == "female_surprise":
            final = "surprise"
        elif final == "female_happy":
            final = "happy"
        elif final == "female_neutral":
            final = "neutral"
        elif final == "female_sad":
            final = "sad"
        elif final == "female_angry":
            final = "angry"
        elif final == "female_fear":
            final = "fear"
        elif final == "female_disgust":
            final = "disgust"
        elif final == "male_surprise":
            final = "surprise"
        elif final == "male_happy":
            final = "happy"
        elif final == "male_neutral":
            final = "neutral"
        elif final == "male_sad":
            final = "sad"
        elif final == "male_angry":
            final = "angry"
        elif final == "male_fear":
            final = "fear"
        elif final == "male_disgust":
            final = "disgust"
        print(final)

        # model = keras.models.load_model(
        #     'C:/Users/91788/Desktop/pro2/backend/media/audio/Emotion_Model2.h5')
        # y_pred = model.predict(
        #     "C:/Users/91788/Desktop/pro2/backend/media/audio/"+name, batch_size=1, verbose=1)
        # print(y_pred)
        # print(model.summary())
        return Response(data={"final": final}, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        instance = studentAudio.objects.all()
        serializer = studentaudioser(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class studentInstanceview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        instance = student.objects.filter(id=pk).first()
        serializer = studentser(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class appUsageInstanceview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        instance = appUsageData.objects.filter(id=pk).first()
        serializer = appusagedataser(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class studentAudioInstanceview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        instance = studentAudio.objects.filter(id=pk).first()
        serializer = studentaudioser(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Feeling(APIView):

    def post(self, request):
        data = request.data
        feeling = data['feeling']
        user = request.user
        date = datetime.now()
        instance = Feeling.objects.create(
            feeling=feeling, user=user, date=date)
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        date = datetime.now()
        if instance:
            instance = Feeling.objects.filter(user=user, date=date).first()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class studentFeelingview(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        feeling = data['feeling']
        user = request.user
        instance = studentFeeling.objects.create(feeling=feeling, user=user)
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        instance = studentFeeling.objects.all()
        serializer = studentFeelingSer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
