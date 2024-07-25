from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 

class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        label="نام",
        max_length=50,
        widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"نام خود را وارد کنید"})
    )
    
    last_name = forms.CharField(
        label="نام خانوادگی",
        max_length=50,
        widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"نام خانوادگی خود را وارد کنید"})
    )
    
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"ایمیل خود را وارد کنید"})
    )
    
    username = forms.CharField(
        label="نام کاربری",
        max_length=20,
        widget=forms.TextInput(attrs={"class":"form-control" ,"placeholder":"نام کاربری "})
    )
    
    password1 = forms.CharField(
        label="رمز",
        max_length=50,
        widget=forms.PasswordInput(attrs={"class":"form-control","name":"password",'type':'password',  "placeholder":"رمز خود را وارد کنید"})
    )
    
    password2 = forms.CharField(
        label="تایید رمز",
        max_length=50,
        widget=forms.PasswordInput(attrs={"class":"form-control","name":"password",'type':'password',  "placeholder":"دوباره رمز خود را وارد کنید"})
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')