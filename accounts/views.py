# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import SignupForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Profile
from .forms import Profile_form,UserForm
from django.urls import reverse



# Create your views here.
def Siginup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    context = {
        'form': form
    }

    return render(request, 'signup.html', context)


def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method =='POST':
        userform = UserForm(request.POST,instance=request.user)
        profile_form = Profile_form(request.POST,instance=profile)
        if userform.is_valid():
            userform.save()
            my_prifile_form=profile_form.save(commit=False)
            my_prifile_form.user = request.user
            my_prifile_form.save()
            return redirect(reverse('accounts:profile'))



    else:
        userform =UserForm(instance=request.user)
        profile_form =Profile_form(instance=profile)
    context = {
        'profile': profile,
        'userform':userform,
        'profile_form':profile_form
    }

    return render(request, 'profile_edit.html', context)
