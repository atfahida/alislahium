from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


def user_logout(request):
    logout(request)
    return redirect("login")