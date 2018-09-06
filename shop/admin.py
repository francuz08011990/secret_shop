from django.contrib import admin

from .models import LeatherSeat, CustomSeat, LimitedSeat, Bag, Bike, Accessories


@admin.register(LeatherSeat)
class LeatherSeatAdmin(admin.ModelAdmin):
    list_display = ('brand', 'price')
    search_fields = ('brand', )
    list_filter = ('price', )


@admin.register(CustomSeat)
class CustomSeatAdmin(admin.ModelAdmin):
    list_display = ('brand', 'price')
    search_fields = ('brand',)
    list_filter = ('price',)


@admin.register(LimitedSeat)
class LimitedSeatAdmin(admin.ModelAdmin):
    list_display = ('brand', 'price')
    search_fields = ('brand',)
    list_filter = ('price',)


@admin.register(Bag)
class BagAdmin(admin.ModelAdmin):
    list_display = ('brand', 'price')
    search_fields = ('brand',)
    list_filter = ('price',)


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('brand', 'price')
    search_fields = ('brand',)
    list_filter = ('price',)


@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ('brand', 'price')
    search_fields = ('brand', )
    list_filter = ('price',)
