from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from django.contrib.auth import password_validation
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def index(request):
    return render(request,'accounts/index.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form=UserCreationForm()
    context={
        'form':form,
    }
    return render(request,'accounts/signup.html',context)


def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            print(request.GET.get('next'))
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form=AuthenticationForm()
    context={
        'form':form,
    }
    return render(request,'accounts/login.html',context)


@login_required
def logout(request):
    if request.method=='POST':
        auth_logout(request)
    return redirect('accounts:index')


@login_required
def update(request):
    if request.method=='POST':
        form=CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form=CustomUserChangeForm(instance=request.user)
    context={
        'form':form,
    }
    return render(request,'accounts/update.html',context)


@login_required
def delete(request):
    if request.method=='POST':
        request.user.delete()
        return redirect('accounts:index')
    return render(request,'accounts/delete.html')

@login_required
def password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('accounts:update')
    else:
        form=PasswordChangeForm(request.user)
    context={
        'form':form,
    }
    return render(request,'accounts/password.html',context)