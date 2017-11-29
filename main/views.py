from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from .models import UserCheck


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            checkedUser = UserCheck.objects.filter(user=user)

            if checkedUser:
                # TODO change about check
                print('checked user')
                return redirect('index')
            else:
                UserCheck.objects.create(user=user)
                print('add user')
                return redirect('vote/')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        if True:
            return render(request, 'main/login.html')
        else:
            return render(request, 'main/Elected.html')


def super_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        super_user = User.objects.filter(is_superuser=True)
        if user is not None and user in super_user:
            return render(request, 'main/super-user.html')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        return render(request, 'main/super-user-login.html')


def super_user_control(request):
    print(request.POST)
    return redirect('index')
