from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Order

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'Property.html', {'orders': orders})

def indexhtml(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def Search(request):
    template = loader.get_template('Search.html')
    return HttpResponse(template.render())

def Booking(request):
    template = loader.get_template('Booking.html')
    return HttpResponse(template.render())

def Contact(request):
    template = loader.get_template('Contact.html')
    return HttpResponse(template.render())

def Explore(request):
    template = loader.get_template('Explore.html')
    return HttpResponse(template.render())

def Listing1(request):
    template = loader.get_template('listing1.html')
    return HttpResponse(template.render())

def Listing2(request):
    template = loader.get_template('listing2.html')
    return HttpResponse(template.render())