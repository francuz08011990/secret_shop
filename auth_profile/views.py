from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import UserProfile


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def all_users(request):
    users = UserProfile.objects.all()
    data = {'users': users}
    return render(request, 'all_users.html', data)


def user_detail(request, pk):
    """
    Функция должна возвращать детальную информацию по пользователю
    """
    userprofile = UserProfile.objects.get(user_id=pk)
    data = {'userprofile': userprofile}
    return render(request, 'user_detail.html', data)


def registration_view(request):
    data = {}
    if request.method == "POST":
        user_data = request.POST
        if user_data['password'] == user_data['confirm_password']:
            try:
                user = User.objects.create_user(
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    password=user_data['password'],
                    email=user_data['email'],
                    username=user_data['email']
                )
                UserProfile.objects.create(user=user)
                data['message'] = 'Вы успешно зарегистрировались на сайте!'
            except:
                data['error'] = 'Данный email уже зарегистрирован!'
        else:
            data['error'] = 'Пароли не совпадают'
    return render(request, 'registration.html', data)


def login_view(request):
    if request.method == "POST":
        login_data = request.POST
        user = authenticate(request, username=login_data['email'], password=login_data['password'])
        if user:
            login(request, user)
            messages.success(request, 'Добро пожаловать')
        else:
            messages.error(request, 'Неправильный пользователь или пароль')
    return redirect(request.META.get('HTTP_REFERER'))


