from shopping.models import *
from .models import *
from django import forms

class UpdateForm_two(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

class UpdateForm_three(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['status']


class CreateDisForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs = {
            'class': 'input', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
            'placeholder':'Name',
        }
    ))
    surname = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs = {
            'class': 'input', 
            'type': 'text',
            'name': 'surname',
            'data-constraints': '@Required',
            'placeholder':'Surname',
        }
    ))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'input', 
            'type': 'text',
            'name': 'phone',
            'data-constraints': '@Required',
            'placeholder':'Phone',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'input',
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
            'placeholder':'Email',
        }
    ))
    area_of_operation = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'input', 
            'type': 'text',
            'name': 'location',
            'data-constraints': '@Required',
            'placeholder':'Area of opreration',
        }
    ))
    class Meta:
        model = Distributor
        fields = '__all__'

class ProductsForm(forms.ModelForm):
    name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs = {
            'class': 'input', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
            'placeholder':'Name',
        }
    ))
    measurement = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs = {
            'class': 'input',
            'type': 'text',
            'name': 'measurement',
            'data-constraints': '@Required',
            'placeholder':'Measurement',
        }
    ))
    price = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            'class': 'input', 
            'type': 'number',
            'name': 'price',
            'data-constraints': '@Required',
            'placeholder':'Price',
        }
    ))
    image = forms.ImageField(widget=forms.ClearableFileInput(
        attrs = {
            'class': 'input',
            'type': 'file',
            'name': 'image',
            'data-constraints': '@Required',
        }
    ))
    class Meta:
        model = Product
        fields = '__all__'

 
