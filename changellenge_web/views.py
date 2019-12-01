from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from changellenge_web import models
from . import forms
import pandas
import numpy as np
import re


# Create your views here.

def add_service(request):
    context = {
        'form': forms.AddServiceForm()
    }
    if request.method == 'POST':
        context['form'] = forms.AddServiceForm(request.POST)
    return render(
        request,
        'changellenge/add-service.html',
        context
    )


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('services'))
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request=request, user=form.get_user())
            return redirect(reverse('services'))
    return render(request, 'changellenge/reg.html', {'form': form})


@login_required(login_url='')
def services(request):
    return render(request, 'changellenge/index.html', {
        'services': models.Services.objects.all(),
        'service_sates': models.Services.service_status,
        'users': [x.first_name + ' ' + x.last_name for x in models.get_user_model().objects.all()],
        'services_name': [x.name for x in models.Services.objects.all()],
        'tags': [x.name for x in models.Tag.objects.all()],
        'form': forms.AddServiceForm()
    })
