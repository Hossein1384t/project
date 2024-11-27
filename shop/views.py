from django.shortcuts import render, redirect
from django.template.context_processors import request

from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# "این پایینی ها مال ثبت نام کردن کاربره"
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


def index (request):
    all_products = Product.objects.all()
    return render(request, 'index.html' , {'products': all_products})

def about (request):
    return render(request, 'about.html')

def login_user (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید')
            return redirect('shop:index')
        else:
            messages.success(request, 'مشکلی در وارد شدن وجود داشت' )
            return redirect('shop:login')
    else:
        return render(request, 'login.html')


def logout_user (request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید')
    return redirect('shop:index')

def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(username=username, password=password1)
            if user:  # مطمئن شوید که احراز هویت موفق بوده است
                login(request, user)
                messages.success(request, 'با موفقیت ثبت نام شدید')
                return redirect('shop:index')
            else:
                messages.error(request, 'مشکلی در ورود به سیستم وجود داشت.')
        else:
            messages.error(request, 'مشکلی در ثبت نام وجود داشت')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def product (request ,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html' , {'product': product})


# def category (request ,cat):
#     cat = cat.replace("_" , " ")
#     try:
#         category = Category.objects.get(name=cat)
#         products = product.objects.filter(category=category)
#         return render(request, 'category.html' , {'products': products , "category": category})
#     except:
#         messages.success(request, ('دسته بندی وجود ندارد'))


def category(request, cat):  
    cat = cat.replace("-", " ")  
    try:  
        category = Category.objects.get(name=cat)  
        products = Product.objects.filter(category=category)  
        return render(request, 'category.html', {'products': products, 'category': category})  
    except Category.DoesNotExist:  
        messages.error(request, 'دسته بندی وجود ندارد')  
        return render(request, 'category.html', {'products': [], 'category': None})