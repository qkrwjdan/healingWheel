from django.urls import path
from .views import register
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',auth_view.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),

]
