from django.shortcuts import render


from .models import LeatherSeat, CustomSeat, LimitedSeat, Bag, Bike, Accessories


def shop(request):
    return render(request, 'shop.html')


def all_leather_seat(request):
    seats = LeatherSeat.objects.all()
    data = {'seats': seats}
    return render(request, 'all_leather_seat.html', data)


def detail_leather_seat(request, pk):
    seat = LeatherSeat.objects.get(id=pk)
    data = {'seat': seat}
    return render(request, 'detail_leather_seat.html', data)


def all_custom_seat(request):
    seats = CustomSeat.objects.all()
    data = {'seats': seats}
    return render(request, 'all_custom_seat.html', data)


def detail_custom_seat(request, pk):
    seat = CustomSeat.objects.get(id=pk)
    data = {'seat': seat}
    return render(request, 'detail_custom_seat.html', data)


def all_limited_seat(request):
    seats = LimitedSeat.objects.all()
    data = {'seats': seats}
    return render(request, 'all_limited_seat.html', data)


def detail_limited_seat(request, pk):
    seat = LimitedSeat.objects.get(id=pk)
    data = {'seat': seat}
    return render(request, 'detail_limited_seat.html', data)


def all_bag(request):
    bags = Bag.objects.all()
    data = {'bags': bags}
    return render(request, 'all_bag.html', data)


def detail_bag(request, pk):
    bag = Bag.objects.get(id=pk)
    data = {'bag': bag}
    return render(request, 'detail_bag.html', data)


def all_bike(request):
    bikes = Bike.objects.all()
    data = {'bikes': bikes}
    return render(request, 'all_bike.html', data)


def detail_bike(request, pk):
    bike = Bike.objects.get(id=pk)
    data = {'bike': bike}
    return render(request, 'detail_bike.html', data)


def all_accessories(request):
    accessories = Accessories.objects.all()
    data = {'accessories': accessories}
    return render(request, 'all_accessories.html', data)


def detail_accessory(request, pk):
    accessory = Accessories.objects.get(id=pk)
    data = {'accessory': accessory}
    return render(request, 'detail_accessory.html', data)
