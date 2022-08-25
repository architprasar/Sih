from rest_framework import serializers
from .models import *

class studentser(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    age = serializers.IntegerField()
    phone = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.age = validated_data.get('age', instance.age)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

    
class appusagedataser(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    appName = serializers.CharField(max_length=100)
    appUsage = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return appUsageData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.appName = validated_data.get('appName', instance.appName)
        instance.appUsage = validated_data.get('appUsage', instance.appUsage)
        instance.save()
        return instance


class studentaudioser(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    audio = serializers.FileField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return studentAudio.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.audio = validated_data.get('audio', instance.audio)
        instance.save()
        return instance


class studentFeelingSer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    feeling = serializers.CharField(max_length=100)
    date = serializers.DateField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return studentFeeling.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.feeling = validated_data.get('feeling', instance.feeling)
        instance.save()
        return instance