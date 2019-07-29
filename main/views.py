from django.shortcuts import render
from .forms import DrivingTimeForm

def index(request):
    return render(request,'main/index.html',)

def aboutus(request):
    return render(request,'main/aboutus.html',)

def loc_ren(request):
    return render(request,'main/loc_ren.html',)

def how_to(request):
    return render(request,'main/how_to.html')

def contact(request):
    return render(request,'main/contact.html')

def charge(request):
    form = DrivingTimeForm()
    return render(request,'main/charge.html',{
    'form' : form
    })
