from django.shortcuts import render
from django.http import JsonResponse

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
