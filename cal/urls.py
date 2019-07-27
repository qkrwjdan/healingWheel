from django.urls import path
from .views import *

urlpatterns = [
    path('/',index,name='home'),
    path('add_income/',add_income,name="add_income"),
    path('add_spending/',add_spending,name="add_spending"),
    path('income_update/<int:pk>',IncomeUpdateView.as_view(),name="income_update"),
    path('income_delete/<int:pk>',IncomeDeleteView.as_view(), name="income_delete"),
    path('spend_update/<int:pk>',SpendUpdateView.as_view(),name="spend_update"),
    path('spend_delete/<int:pk>',SpendDeleteView.as_view(), name="spend_delete"),
]
