from django.contrib import admin

from .models import LeatherSeat, CustomSeat, LimitedSeat, Bag, Bike, Accessories


class LeatherSeatAdmin(admin.ModelAdmin):
    pass


class CustomSeatAdmin(admin.ModelAdmin):
    pass


class LimitedSeatAdmin(admin.ModelAdmin):
    pass


class BagAdmin(admin.ModelAdmin):
    pass


class BikeAdmin(admin.ModelAdmin):
    pass


class AccessoriesAdmin(admin.ModelAdmin):
    pass

admin.site.register(LeatherSeat, LeatherSeatAdmin)
admin.site.register(CustomSeat, CustomSeatAdmin)
admin.site.register(LimitedSeat, LimitedSeatAdmin)
admin.site.register(Bag, BagAdmin)
admin.site.register(Bike, BikeAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
