from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('add-customer',views.add_customer,name='add_customer'),
    path('edit-customer/<int:pk>/',views.edit_customer,name='edit_customer'),
    path('delete-customer/<int:pk>/',views.delete_customer,name='delete_customer'),
    path('view-customer',views.view_customer,name='view_customer'),
    path('new-booking',views.new_booking,name='new_booking'),
    path('rental-details',views.rental_details,name='rental_details'),
    path('view-inventory',views.view_inventory,name='view_inventory'),
    path('add-inventory',views.add_inventory,name='add_inventory'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    # path('add-customer',views.add_customer,name='add_customer'),
    
]
