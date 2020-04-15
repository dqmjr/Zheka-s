from django.shortcuts import render
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def signUpPage(request):
    form = SignupForm()
    return render(request, 'signup.html', {"form": form})


def signUp(request):
    form = SignupForm(request.POST)
    if form.is_valid():
        user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.save()
        return HttpResponseRedirect('/login')

    return HttpResponseRedirect('/signup?error=1')


def logInPage(request):
    form = LoginForm()
    return render(request, 'login.html', {"form": form})


def logIn(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/login?error=2')
    return HttpResponseRedirect('/login?error=1')


def logOut(request):
    logout(request)
    return HttpResponseRedirect('/')