from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    birth = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
class Course(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='courses/')
    description = models.TextField()

    def __str__(self):
        return self.name    