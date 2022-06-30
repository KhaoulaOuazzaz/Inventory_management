from django import forms
from django.forms import fields
from .models import Product, Order, Provider


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','quantity','category']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['state']


class ProviderForm(forms.ModelForm):
     class Meta:
            model = Provider
            fields = ['p_name','p_phone','p_web','p_mail','p_ados']


class OrderForm1(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','order_quantity']