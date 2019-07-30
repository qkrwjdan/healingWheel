from django.shortcuts import render
from .forms import DrivingTimeForm
from django.contrib.auth.decorators import login_required

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
        form = DrivingTimeForm()
        if form.is_valid():
            if request.POST['detail_menu'] == '10':
                return render(request,'main/index.html')
            elif request.POST['detail_menu'] == '30':
                return render(request,'main/index.html')
            else:
                return render(request,'main/index.html')
    else:
        form = DrivingTimeForm()

    return render(request,'main/charge.html',{
    'form' : form
    })

def profile(request):
    return render(request,'main/profile.html')
