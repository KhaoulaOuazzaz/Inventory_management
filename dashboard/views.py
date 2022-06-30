from typing import ContextManager
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product,Order, Provider
from .forms import OrderForm1, ProductForm, OrderForm, ProviderForm
from django.contrib.auth.models import User
# Create your views here.

from django.contrib import messages

@login_required
def index(request):
   orders = Order.objects.all()
   products = Product.objects.all()
   orders_count = orders.count()
   products_count = products.count()
   workers_count = User.objects.all().count()
   providers_count = Provider.objects.all().count()
   if request.method=='POST':
      form = OrderForm1(request.POST)
      if form.is_valid():
         instance= form.save(commit=False)
         instance.staff = request.user
         instance.save()
         return redirect('dashboard-index')
   else:
         form = OrderForm1()
   context={
      'orders': orders,
      'form' : form,
      'products': products,
      'orders_count':orders_count,
      'products_count':products_count,
      'workers_count':workers_count,
      'providers_count':providers_count,
   }
   return render(request,'dashboard/index.html',context)






@login_required
def staff(request):
   workers = User.objects.all()
   workers_count = workers.count()
   providers_count = Provider.objects.all().count()
   orders_count = Order.objects.all().count()
   products_count = Product.objects.all().count()
   context={
      'workers': workers,
      'workers_count':workers_count,
      'providers_count':providers_count,
      'orders_count':orders_count,
      'products_count':products_count,
   }
   return render(request,'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
   worker = User.objects.get(id=pk)
   context = {
      'worker' : worker,
   }
   return render(request,'dashboard/staff_detail.html',context)


@login_required
def staff_delete(request, pk):
   worker = User.objects.get(id=pk)
   if request.method=='POST':
      worker.delete()
      return redirect('dashboard-staff')
   return render(request,'dashboard/staff_delete.html')



@login_required
def product(request):
   items = Product.objects.all()
   products_count = items.count()
   workers_count = User.objects.all().count()
   providers_count = Provider.objects.all().count()
   orders_count = Order.objects.all().count()
   if request.method == 'POST':
      form = ProductForm(request.POST)
      if form.is_valid():
         form.save()
         product_name = form.cleaned_data.get('name')
         messages.success(request, f'{product_name} has been added')
         return redirect('dashboard-product')
   else:
      form = ProductForm()
   context = {
      'items' : items,
      'form' : form,
      'workers_count': workers_count,
      'providers_count':providers_count,
      'orders_count':orders_count,
      'products_count':products_count,
   }
   return render(request,'dashboard/product.html', context)


@login_required
def product_delete(request, pk):
   item = Product.objects.get(id=pk)
   if request.method=='POST':
      item.delete()
      return redirect('dashboard-product')
   return render(request,'dashboard/product_delete.html')




@login_required
def product_update(request, pk):
   item= Product.objects.get(id=pk)
   if request.method=='POST':
      form = ProductForm(request.POST, instance=item)
      if form.is_valid():
         form.save()
         return redirect('dashboard-product')
   else:
    form = ProductForm(instance=item)
   context={
      'form' : form,
   }
   return render(request,'dashboard/product_update.html',context)





@login_required
def order(request):
   orders = Order.objects.all()
   orders_count = orders.count()
   workers_count = User.objects.all().count()
   providers_count = Provider.objects.all().count()
   products_count = Product.objects.all().count()
   context={
      'orders':orders,
      'workers_count':workers_count,
      'providers_count':providers_count,
      'orders_count':orders_count,
      'products_count':products_count,
   }
   return render(request,'dashboard/order.html',context)

@login_required
def order_delete(request, pk):
   item = Order.objects.get(id=pk)
   if request.method=='POST':
      item.delete()
      return redirect('dashboard-order')
   return render(request,'dashboard/order_delete.html')

@login_required
def order_update(request, pk):
   item= Order.objects.get(id=pk)
   if request.method=='POST':
      form = OrderForm(request.POST, instance=item)
      if form.is_valid():
         form.save()
         return redirect('dashboard-order')
   else:
    form = OrderForm(instance=item)
   context={
      'form' : form,
   }
   return render(request,'dashboard/order_update.html',context)






@login_required
def provider(request):
   prov = Provider.objects.all()
   providers_count = prov.count()
   workers_count = User.objects.all().count()
   orders_count = Order.objects.all().count()
   products_count = Product.objects.all().count()
   if request.method == 'POST':
      form = ProviderForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('dashboard-provider')
   else:
      form = ProviderForm()   
   context = {
      'prov' : prov,
      'form' : form,
      'workers_count':workers_count,
      'providers_count':providers_count,
      'orders_count':orders_count,
      'products_count':products_count,
   }
   return render(request,'dashboard/provider.html', context)


@login_required
def provider_delete(request, pk):
   item = Provider.objects.get(id=pk)
   if request.method=='POST':
      item.delete()
      return redirect('dashboard-provider')
   return render(request,'dashboard/provider_delete.html')

@login_required
def provider_update(request, pk):
   prov= Provider.objects.get(id=pk)
   if request.method=='POST':
      form = ProviderForm(request.POST, instance=prov)
      if form.is_valid():
         form.save()
         return redirect('dashboard-provider')
   else:
    form = ProviderForm(instance=prov)
   context={
      'form' : form,
   }
   return render(request,'dashboard/provider_update.html',context)