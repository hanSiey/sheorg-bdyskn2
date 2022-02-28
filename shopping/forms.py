from .models import ClientMessage, Customer
from django import forms

class CheckoutForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'name', 
            'type': 'text',
            'name': 'name',
            'value': ' ',
            
        }
    ))
    surname = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'surname', 
            'type': 'text',
            'name': 'surname',
            'value': ' ',
            
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'email', 
            'type': 'text',
            'name': 'email',
            'value': ' ',
            'data-constraints': '@Email',
        }
    ))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'phone', 
            'type': 'text',
            'name': 'phone',
            'value': ' ',
            
        }
    ))
    address= forms.CharField(max_length=100, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'adrress', 
            'type': 'text',
            'name': 'address',
            
            
        }
    ))
    city = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'city', 
            'type': 'text',
            'name': 'city',
            
        }
    ))
    state = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'state', 
            'type': 'text',
            'name': 'state',
            
            
        }
    ))
    zipcode = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'zipcode', 
            'type': 'text',
            'name': 'zipcode',
            
        }
    ))
    class Meta:
        model = Customer
        fields = '__all__'

class messageform(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'first_name', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
        }
    ))
    surname = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'last_name', 
            'type': 'text',
            'name': 'surname',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'id': 'email_address', 
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
        }
    ))
    message = forms.CharField(max_length=100000000, widget=forms.Textarea(
        attrs = {
            'class': 'form-control',
            'id': 'message', 
            'type': 'text',
            'name': 'message',
            'data-constraints': '@Required',
        }
    ))
    class Meta:
        model = ClientMessage
        fields = '__all__'


class CreateUser(forms.Form):
    name = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-control', 
            'id':'first_name',
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
        }
    ))
    surname = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-control', 
            'id':'last_name',
            'type': 'text',
            'name': 'surname',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'id':'email_address',
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
        }
    ))
    phone = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id':'phone',
            'type': 'phone',
            'name': 'phone',
            'data-constraints': '@Required',
        }
    ))
    password1 = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id':'password',
            'type': 'password',
            'name': 'password1',
            'data-constraints': '@Required',
        }
    ))
    password2 = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id':'confirm_passowrd', 
            'type': 'password',
            'name': 'password2',
            'data-constraints': '@Required',
        }
    ))

class LogInForm(forms.Form):
    name = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id':'first_name', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'id':'email_address',
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
        }
    ))
    password1 = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id':'password',
            'type': 'password',
            'name': 'password1',
            'data-constraints': '@Required',
        }
    ))