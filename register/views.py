from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

        return redirect("/ohno")

    else:
        form = UserCreationForm()
    
    return render(request, "register.html", {"form":form})

def invalid_form_view(request):
    return render(request, "bad.html")
