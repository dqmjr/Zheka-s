from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password =  forms.CharField(max_length=100, widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password =  forms.CharField(max_length=100, widget=forms.PasswordInput())