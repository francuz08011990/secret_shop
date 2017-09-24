from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .models import UserProfile


def all_users(request):
    users = UserProfile.objects.all()
    template_name = 'all_users.html'
    data = {'users': users}
    return render(request, template_name, data)


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def user_detail(request, pk):
    """
    Функция должна возвращать детальную информацию по пользователю
    """
    userprofile = UserProfile.objects.get(user_id=pk)
    template_name = 'user_detail.html'
    data = {'userprofile': userprofile}
    return render(request, template_name, data)


def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)


def registration_view(request):
    template_name = 'registration.html'
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
    return render(request, template_name, data)


def login_view(request):
    if request.method == "POST":
        login_data = request.POST
        user = authenticate(request, username=login_data['email'], password=login_data['password'])
        if user:
            login(request, user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


