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


def fisher_wagner(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x - 1] == seq2[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1)
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,  # удаление
                    matrix[x - 1, y - 1] + 1,  # замена
                    matrix[x, y - 1] + 1)  # вставка
    return matrix[size_x - 1, size_y - 1]


def fisher_wagner_lst(src, dst):
    src = re.split(r'[ \t\n\r\v\f]', src)
    dst = re.split(r'[ \t\n\r\v\f]', dst)
    diff = 0
    for d in dst:
        for s in src:
            diff += fisher_wagner(d, s)
    return diff


def liven_test(request):
    df = pandas.DataFrame([
        {'about': x.about, 'id': x.id, 'name': x.name} for x in models.Services.objects.all()])
    df['diff'] = df.apply(lambda x: fisher_wagner_lst(x[0], request.GET.get('test', '')), axis=1)
    return HttpResponse(
        f'<form><textarea name="test"></textarea><button>Kek</button></form><br><pre>{str(df.sort_values("diff").head(10))}</pre>'
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
    return render(request, 'changellenge/index.html')
