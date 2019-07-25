from django.shortcuts import render

def index(request):
    return render(request,'main/index.html',)

def aboutus(request):
    return render(request,'main/aboutus.html',)

def loc_ren(request):
    return render(request,'main/loc_ren.html',)
