from django.db import models

from student.models import student

# Create your models here.
class parent(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

