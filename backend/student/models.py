from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class appUsageData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appName = models.CharField(max_length=50)
    appUsage = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.appName


class studentAudio(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audio/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mood = models.CharField(max_length=50)

    def __str__(self):
        return self.audio.name


class Feeling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feeling = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.audio.name


class studentFeeling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feeling = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.feeling
