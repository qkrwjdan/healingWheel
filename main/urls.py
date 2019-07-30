from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('loc_ren',views.loc_ren,name='loc_ren'),
    path('how_to',views.how_to,name='how_to'),
    path('contact',views.contact,name='contact'),
    path('charge',views.charge,name='charge'),
    path('profile',views.profile,name='profile'),

]
