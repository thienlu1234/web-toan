from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile, Course, Lesson
def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})


def courses(request):
    return render(request, 'courses.html')


# REGISTER
def register_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        birth = request.POST.get('birth')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Tài khoản đã tồn tại'
            })

        if password != confirm_password:
            return render(request, 'register.html', {
                'error': 'Mật khẩu không khớp'
            })

        # tạo user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.first_name = fullname
        user.save()

        # tạo profile
        Profile.objects.create(
            user=user,
            phone=phone,
            gender=gender,
            birth=birth
        )

        login(request, user)
        return redirect('home')

    return render(request, 'register.html')

# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'error': 'Sai tài khoản hoặc mật khẩu'
            })

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')
def course_detail(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'course_detail.html', {'course': course})

def course_detail(request, id):
    course = Course.objects.get(id=id)
    lessons = Lesson.objects.filter(course=course)

    return render(request, 'course_detail.html', {
        'course': course,
        'lessons': lessons
    })
def lesson_detail(request, id):
    lesson = Lesson.objects.get(id=id)

    return render(request, 'lesson_detail.html', {
        'lesson': lesson
    })