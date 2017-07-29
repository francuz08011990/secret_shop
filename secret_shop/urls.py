from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from auth_profile.views import *


urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('auth_profile.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^contact/', contact, name='contact'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
