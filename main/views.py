from django.shortcuts import render,redirect
from .forms import DrivingTimeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import timedelta

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

@login_required
def charge(request):
    if request.method == 'POST':
        us = request.user
        profile = us.profile
        if request.POST['detail_menu'] == '10':
            profile.duration += timedelta(minutes = 10)
        elif request.POST['detail_menu'] == '30':
            profile.duration += timedelta(minutes = 30)
        else:
            profile.duration += timedelta(minutes = 60)
        profile.save()
        return redirect('profile')

    return render(request,'main/charge.html',{
    })

@login_required
def profile(request):
    us = request.user
    return render(request,'main/profile.html',{
    'user' : us
    })
