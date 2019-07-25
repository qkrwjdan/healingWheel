from django.shortcuts import render,get_object_or_404,redirect
from .models import Income,spending
from .forms import IncomeForm,SpendForm
from django.views.generic.edit import DeleteView,UpdateView
from django.urls import reverse_lazy

def index(request):
    income = Income.objects.all()
    spend = spending.objects.all()

    result = 0

    for i in income:
        result = result + i.money

    for i in spend:
        result = result - i.money

    return render(request,'cal/index.html',{
    'income' : income , 'spend' : spend , 'result' : result ,
    })

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit = False)
            income.save()
            return redirect('index')
    else:
        form = IncomeForm()
    return render(request,'cal/add_income.html',{
    'form' : form
    })

def add_spending(request):
    if request.method == 'POST':
        form = SpendForm(request.POST)
        if form.is_valid():
            spend = form.save(commit = False)
            spend.save()
            return redirect('index')
    else:
        form = SpendForm()
    return render(request,'cal/add_spending.html',{
    'form' : form
    })

class IncomeDeleteView(DeleteView):
    model = Income
    success_url = reverse_lazy('index')

class SpendDeleteView(DeleteView):
    model = spending
    success_url = reverse_lazy('index')

class IncomeUpdateView(UpdateView):
    model = Income
    fields = ['name','money']
    template_name_suffix = '_update'

class SpendUpdateView(UpdateView):
    model = spending
    fields = ['name','money']
    template_name_suffix = '_update'
