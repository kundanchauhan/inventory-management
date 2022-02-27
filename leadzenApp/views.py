from multiprocessing import context
from django.shortcuts import render, HttpResponse
import datetime
from .models import *
from leadzenApp.models import *
from django.contrib import messages
import json

from django.http import JsonResponse
# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def add_customer(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        onboard_date = datetime.now()
        print(name,email)
        customer_obj = add_customer_details(name=name,email=email,phone_number=phone_number,onboard_date=onboard_date)
        customer_obj.save()
        message = 'Customer Details add successfully.'
        messages.success(request, message)
    return render(request,'add_customer.html')


def edit_customer(request):        
    return render(request,'edit_customer.html')

def delete_customer(request, pk): 
    customer_obj= add_customer_details.objects.filter(id=pk)
    context = {'customer_obj': customer_obj}
    # customer_obj.save()
    print(pk)      
    print(customer_obj) 
    delete_customer
    if request.method == "POST":
        customer_del_obj= add_customer_details.objects.filter(id=pk).delete()
        customer_obj = add_customer_details.objects.all()
        print(customer_obj)
        context={'customer_obj':customer_obj}
        message = 'Customer Details Delete successfully.'
        messages.success(request, message)
        return render(request,'view_customer.html',context)

    return render(request,'delete_customer.html',context)



def view_customer(request):
    customer_obj = add_customer_details.objects.all()
    print(customer_obj)
    context={'customer_obj':customer_obj}
    for i in customer_obj:
        print(i.id)
    return render(request,'view_customer.html',context)





def autocomplete(request):
    if 'term' in request.GET:
        print(request.GET.get('term'))
        qs = add_customer_details.objects.filter(name__icontains = request.GET.get('term'))
       
        print("qsssssss",qs)
        titles = list()
        for product in qs:
            titles.append(product.name)
       
        return JsonResponse(titles, safe=False)
    return render(request, 'new_booking.html.html')

def new_booking(request):
    if request.method == "POST":
        customer_name =request.POST['product']
        vehical_name =request.POST['vehical_type']
        vehical_number =request.POST['vehical_number']
        bike_obj = inventory.objects.filter(vehical_name = 'bike').count()
        cycle_obj = inventory.objects.filter(vehical_name = 'cycle').count()
        cars_obj = inventory.objects.filter(vehical_name = 'car').count()
        boat_obj = inventory.objects.filter(vehical_name = 'boat').count()
        if vehical_name == 'bike':
            if bike_obj > 2 :
                message = 'All Bikes Already Booked. '
                messages.success(request, message)
        elif vehical_name == 'cycle':
            if cycle_obj > 3:
                message = 'All Cycles Already Booked. '
                messages.success(request, message)
        elif vehical_name == 'car':
            if cars_obj > 1:
                message = 'All Cars Already Booked. '
                messages.success(request, message) 
        elif vehical_name == 'boat':
            if boat_obj > 2:
                message = 'All Boats Already Booked. '
                messages.success(request, message)
        customer_obj = add_customer_details.objects.get(name = customer_name)
       
        customer_name = customer_obj.name
        customer_email = customer_obj.email
        phone_number = customer_obj.phone_number
        print(customer_name)
        booking_details_obj = booking_details(vehical_name=vehical_name,vehical_number=vehical_number,name=customer_name,email=customer_email,phone_number=phone_number,booking_date= datetime.now())
        booking_details_obj.save()
        message = 'Booking done successfully. '
        messages.success(request, message)
    
          
        
    return render(request,'new_booking.html')

def rental_details(request):
    booking_obj = booking_details.objects.all()
    print(booking_obj)
    context={'booking_obj':booking_obj}
    return render(request,'rental_details.html',context)


def view_inventory(request):
    
    bike_obj = inventory.objects.filter(vehical_name = 'bike').count()
    cycle_obj = inventory.objects.filter(vehical_name = 'cycle').count()
    cars_obj = inventory.objects.filter(vehical_name = 'car').count()
    boat_obj = inventory.objects.filter(vehical_name = 'boat').count()
    
    booked_bike_obj = booking_details.objects.filter(vehical_name = 'bike').count()
    booked_cycle_obj = booking_details.objects.filter(vehical_name = 'cycle').count()
    booked_cars_obj = booking_details.objects.filter(vehical_name = 'car').count()
    booked_boat_obj = booking_details.objects.filter(vehical_name = 'boat').count()
    print("cycle_obj",cycle_obj)
    print(booked_cycle_obj)
    remaining_bike = bike_obj - booked_bike_obj
    remaining_cycle = cycle_obj  - booked_cycle_obj
    
    remaining_car = cars_obj - booked_cars_obj
    remaining_boat = boat_obj - booked_boat_obj 
    context={'remaining_bike':remaining_bike,'remaining_cycle':remaining_cycle,'remaining_car':remaining_car,'remaining_boat':remaining_boat}
    return render(request,'view_inventory.html',context)

def add_inventory(request):
    
    if request.method == "POST":
        vehical_name = request.POST['vehical_name']
        vehical_number = request.POST['vehical_number']
        print(vehical_name,vehical_number)
        inventory_add_date = datetime.now()
        inventory_obj1 = inventory.objects.filter().all()
        print(inventory_obj1)
        bike_obj = inventory.objects.filter(vehical_name = 'bike').count()
        cycle_obj = inventory.objects.filter(vehical_name = 'cycle').count()
        cars_obj = inventory.objects.filter(vehical_name = 'car').count()
        boat_obj = inventory.objects.filter(vehical_name = 'boat').count()

        
        if vehical_name == 'bike':
            if bike_obj == 2 :
                message = 'You can not add more than 2 Bikes. '
                messages.success(request, message)
        elif vehical_name == 'cycle':
            if cycle_obj == 3:
                message = 'You can not add more than 3 Cycles. '
                messages.success(request, message)
        elif vehical_name == 'car':
            if cars_obj == 1:
                message = 'You can not add more than 1 Car. '
                messages.success(request, message) 
        elif vehical_name == 'boat':
            if boat_obj == 2:
                message = 'You can not add more than 2 Boats. '
                messages.success(request, message)
        
        inventory_obj = inventory(vehical_name=vehical_name,vehical_number=vehical_number,inventory_add_date=inventory_add_date)
        inventory_obj.save()
        print("inventory_obj",inventory_obj)
        message = 'Inventory Details Add successfully. '
        messages.success(request, message)
                     
    return render(request,'add_inventory.html')

