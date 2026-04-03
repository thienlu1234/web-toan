from django.db import models
from django.contrib.auth.models import User
import re

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
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_embed_url(self):
        if not self.video_url:
            return ""

        url = self.video_url.strip()

        if "youtube.com/watch?v=" in url:
            video_id = url.split("watch?v=")[-1].split("&")[0]
            return f"https://www.youtube.com/embed/{video_id}"

        if "youtu.be/" in url:
            video_id = url.split("youtu.be/")[-1].split("?")[0]
            return f"https://www.youtube.com/embed/{video_id}"

        if "youtube.com/embed/" in url:
            return url

        return ""