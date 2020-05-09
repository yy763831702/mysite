from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
def home(request):
    return render(request, 'main/home.html')

def register(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"New Account Created:{username}")
            login(request, user)
            messages.info(request, f"you are now logged in as {username}")

            return redirect("main:home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: form.error_messages[msg]")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})
    form = NewUserForm
    return render(request, "main/register.html", context = {"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Loggout successfully")
    return redirect("main:home")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                messages.info(request, "you are now logged in as {username}")
                login(request, user)
                return redirect("main:home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})
