from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^all_users/$', all_users, name='all_users'),
    url(r'^user/(?P<pk>[0-9]+)$', user_detail, name='user_detail'),
]
