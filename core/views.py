from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def courses(request):
    return render(request, 'courses.html')


# REGISTER
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # kiểm tra user tồn tại
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Tài khoản đã tồn tại'
            })

        # tạo user
        user = User.objects.create_user(username=username, password=password)

        # auto login sau khi đăng ký
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