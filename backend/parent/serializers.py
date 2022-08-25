from rest_framework import serializers
from .models import *


class TaskSer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
