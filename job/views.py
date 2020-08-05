# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from .models import Job, Category
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .form import ApplyForms, Jo_Form
from .fillters import ProductFilter

# Create your views here.
def Job_List(request):
    job_list = Job.objects.all()
    my_filter =  ProductFilter(request.GET, queryset=job_list)
    job_list = my_filter.qs
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'job_list': page_obj,
        'my_filter':my_filter,

    }
    return render(request, 'job_list.html', context)

def jo_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form1 = ApplyForms(request.POST, request.FILES)
        if form1.is_valid():
            my_form = form1.save(commit=False)
            my_form.job = job_detail
            my_form.save()
    else:
        form1 = ApplyForms()
    context = {'fform': form1,
               'job_detail': job_detail}
    return render(request, 'job_details.html', context)
@login_required


def addjob(request):
    if request.method == 'POST':
        form = Jo_Form(request.POST,request.FILES)
        if form.is_valid():
            my_jobform = form.save(commit=False)
            my_jobform.owner = request.user
            my_jobform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = Jo_Form()
    context = {
        'form': form,

    }
    return render(request, 'job_add.html', context)
