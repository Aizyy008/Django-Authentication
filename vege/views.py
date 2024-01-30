from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Receipe

def create_receipe(data):
    name = data.get("receipe_name")
    desc = data.get("receipe_description")
    img = data.get("receipe_image")

    Receipe.objects.create(
        receipe_name=name,
        receipe_description=desc,
        receipe_image=img
    )

    return [{"name": name, "desc": desc, "img": img}]

@login_required(login_url="/login/")
def receipes(request):
    receipe_data = []  # Initialize the variable outside the if block

    if request.method == "POST":
        receipe_data = create_receipe(request.POST)
        return redirect("/receipes/")

    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))

    return render(request, "receipes.html", context={"receipes": queryset})

@login_required(login_url="/login/")
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipes/")

@login_required(login_url="/login/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        name = data.get("receipe_name")
        desc = data.get("receipe_description")
        img = request.FILES.get("receipe_image")
        
        queryset.receipe_name = name
        queryset.receipe_description = desc
        if img:
            queryset.receipe_image = img
            
        queryset.save()
        return redirect("/receipes/")
    return render(request, "update-receipe.html", context={"receipe":queryset})


def login_page(request):
    
    if request.method == "POST":
        get_username = request.POST.get("username")
        get_password = request.POST.get("password")
    
    
        if not User.objects.filter(username = get_username).exists():
            messages.error(request, "Invalid Username")
            return redirect("/login/")

        user  = authenticate(username = get_username, password = get_password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login/")
    
        else:
            login(request,user) 
            return redirect("/receipes/")
    return render(request, "login.html")
     
def logout_page(request):
    logout(request)
    return redirect("/login")
    


def register(request):
    # Guard clause to handle non-POST requests
    if request.method != "POST":
        return render(request, "register.html")

    # Handle POST requests
    get_first_name = request.POST.get("first_name")
    get_last_name = request.POST.get("last_name")
    get_username = request.POST.get("username")
    get_password = request.POST.get("password")

    
    
    user = User.objects.filter(username = get_username)
    if user.exists():
        messages.info(request, "Username already exists")
        return redirect("/register/")
    
    
    user = User.objects.create(
        first_name = get_first_name,
        last_name = get_last_name,
        username = get_username,
        
    )
    user.set_password(get_password)
    user.save()
    messages.info(request, "Account created successfully")

    return redirect("/register/")
