import re
from django import forms
from .models import *
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your username', 'id': 'username', 'class': 'px-7 py-1 rounded-full shadow-lg border border-slate-300 ml-3'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter your password', 'id': 'password', 'class': 'px-7 py-1 rounded-full shadow-lg border border-slate-300 ml-3'}))


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not username or not password:
            raise ValidationError('Please enter both username and password.')

        username_pattern = r'^[a-zA-Z0-9_]{3,16}$'
        password_pattern = r'^(?=.*\d)(?=.*[a-zA-Z]).{8,}$'

        if not re.match(username_pattern, username):
            raise ValidationError(
                'Invalid username format. Use only letters, numbers, and underscores (3-16 characters).')

        if not re.match(password_pattern, password):
            raise ValidationError(
                'Invalid password format. Password must be at least 8 characters long and contain at least one letter and one digit.')

        user = authenticate(username=username, password=password)
        if user is None or not user.is_active:
            raise ValidationError('Invalid username or password.')

        return cleaned_data


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['image','unique_id','name','designation','phone','district','chapter','validity_date']
        widgets = {
            'image' : forms.FileInput(attrs={'class': 'hidden', 'accept': 'image/*', 'onchange': 'displayImagePreview(this)'}),
            'name' : forms.TextInput(attrs={'placeholder':'Enter name','class':'form-control block w-[60vw] sm:w-[20vw] py-2 lg:py-2 pl-4 placeholder-gray-500 bg-gray-200 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  rounded-full '}),
            'designation':forms.TextInput(attrs={'placeholder':'Designation','class': 'form-control block w-[60vw] sm:w-[20vw] py-2 lg:py-2 pl-4 placeholder-gray-500 bg-gray-200 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  rounded-full '}),
            'phone': forms.TextInput(attrs={'placeholder':'Phone number', 'pattern': '[6-9]\d{9}','class':'form-control block w-[60vw] sm:w-[20vw] py-2 lg:py-2 pl-4 placeholder-gray-500 bg-gray-200 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  rounded-full '}),
            'chapter' : forms.TextInput(attrs={'placeholder':'Chapter','class':'form-control block w-[60vw] sm:w-[20vw] py-2 lg:py-2 pl-4 placeholder-gray-500 bg-gray-200 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  rounded-full '}),
            'unique_id': forms.TextInput(attrs={'placeholder':'ID', 'name':'unique_id', 'id':'unique_id','class':'form-control block w-[60vw] sm:w-[20vw] py-2 lg:py-2 pl-4 placeholder-gray-500 bg-gray-200 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  rounded-full '}),
            'validity_date':forms.DateInput(attrs={'placeholder':'Registration date','class':'form-control block w-[60vw] sm:w-[20vw] py-2 lg:py-2 pl-4 placeholder-gray-500 bg-gray-200 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  rounded-full '}),
            'district': forms.TextInput(attrs={'placeholder':'District','class':'form-control block w-[60vw] sm:w-[20vw] py-2 lg:py-2 pl-4 placeholder-gray-500 bg-gray-200 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  rounded-full '}),


  }