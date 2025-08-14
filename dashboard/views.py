from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="dashboard:login")
def index(request):
    return render(request, "admin/index.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard:index")
        else:
            messages.error(request, "invalid credentials")
            return redirect("dashboard:login")

    return render(request, "admin/login.html")

def logout(request):
    auth.logout(request)
    return redirect("dashboard:login")
