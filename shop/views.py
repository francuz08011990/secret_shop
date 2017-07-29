from django.shortcuts import render

def shop(request):
    template_name = 'shop.html'
    return render (request, template_name)
