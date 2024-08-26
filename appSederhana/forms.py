from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import EmployeeAdd, new_user
from django.contrib.auth.forms import AuthenticationForm

class registrationForm(UserCreationForm): 
    class Meta:
        model = new_user
        fields=['full_name', 'birth_date']
        widgets = {
            'password' : forms.PasswordInput(),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeAdd
        fields = ['nip','first_name', 'last_name', 'gender', 'birth_place', 'birth_date',
        'address', 'phone_number', 'email', 'date_joined']
        widgets = {
            'nip' : forms.TextInput(attrs={'readonly':'readonly'}),
            'address': forms.Textarea(attrs={
            'placeholder': 'Enter your address here'}),
        }

class RegistForm(forms.ModelForm):
    class Meta:
        model = new_user
        fields = ['full_name', 'birth_date', 'email', 'password']

class LoginForm(AuthenticationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = new_user
        fields = ['email', 'password']