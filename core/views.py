from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def courses(request):
    return render(request, 'courses.html')


# 👉 REGISTER
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Tài khoản đã tồn tại')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Đăng ký thành công')
        return redirect('login')

    return render(request, 'register.html')


# 👉 LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Sai tài khoản hoặc mật khẩu')

    return render(request, 'login.html')


# 👉 LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')