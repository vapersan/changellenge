from django.shortcuts import render
from . import forms


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
