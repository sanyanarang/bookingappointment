from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        contact=Contact()
        name= request.POST.get('name')
        gender= request.POST.get('gender')
        number= request.POST.get('number')
        email= request.POST.get('email')
        date= request.POST.get('date')
        time= request.POST.get('time')
        disease= request.POST.get('disease')
        address= request.POST.get('email')
        contact.name=name
        contact.gender=gender
        contact.number=number
        contact.email=email
        contact.date=date
        contact.time=time
        contact.disease=disease
        contact.address=address
        contact.save()  
        return HttpResponse("<h1>YOUR APPOINTMENT IS BOOKED</h1>")

    return render(request,"index.html") 