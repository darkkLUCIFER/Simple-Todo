from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            email = cd['email']
            password = cd['password']
            user = User.objects.create_user(username, email, password)
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'یوزر با موفقیت ساخته شد.', extra_tags='success')
            return redirect('home:home')

    else:
        form = UserRegisterForm()
    return render(request, 'account/user_register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدید.', extra_tags='success')
                return redirect('home:home')
            else:
                messages.error(request, 'اطلاعات وارد شده صحیح نمیباشد.', 'dnager')
    else:
        form = UserLoginForm()
    return render(request, 'account/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'خارج شدید.', extra_tags='success')
    return redirect('home:home')
