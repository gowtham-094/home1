from django.urls import path
from . import views
urlpatterns = [
        path('home/',views.indexhtml, name='home.html'),
        path('home/property',views.order_list, name='Property'),
        path('home/search',views.Search, name='Search'),
        path('home/booking',views.Booking, name='Booking'),
        path('home/contact',views.Contact,name='Contact'),
        path('home/explore',views.Explore,name='Explore'),
        path('home/listing1',views.Listing1,name='Listing1'),
        path('home/listing2',views.Listing2,name='Listing2'),

]
