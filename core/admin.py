from django.contrib import admin
from .models import Profile
from .models import Course
from .models import Course, Profile, Lesson

admin.site.register(Lesson)
admin.site.register(Profile)
# Register your models here.


admin.site.register(Course)