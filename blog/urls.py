from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', articles, name='articles'),
    url(r'^detail/(?P<pk>[0-9]+)$', article_detail, name='article_detail'),
    url(r'^create_article/', create_article, name='create_article'),
]