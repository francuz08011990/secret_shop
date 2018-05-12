from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', shop, name='shop'),
    url(r'^all_leather_seat/', all_leather_seat, name='all_leather_seat'),
    url(r'^leather_seat/(?P<pk>[0-9]+)$', detail_leather_seat, name='detail_leather_seat'),
    url(r'^all_custom_seat/', all_custom_seat, name='all_custom_seat'),
    url(r'^custom_seat/(?P<pk>[0-9]+)$', detail_custom_seat, name='detail_custom_seat'),
    url(r'^all_limited_seat/', all_limited_seat, name='all_limited_seat'),
    url(r'^limited_seat/(?P<pk>[0-9]+)$', detail_limited_seat, name='detail_limited_seat'),
    url(r'^all_bag/', all_bag, name='all_bag'),
    url(r'^bag/(?P<pk>[0-9]+)$', detail_bag, name='detail_bag'),
    url(r'^all_bike/', all_bike, name='all_bike'),
    url(r'^bike/(?P<pk>[0-9]+)$', detail_bike, name='detail_bike'),
    url(r'^all_accessories/', all_accessories, name='all_accessories'),
    url(r'^accessory/(?P<pk>[0-9]+)$', detail_accessory, name='detail_accessory')
]
