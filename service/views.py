from django.shortcuts import render
from .models import *
# Create your views here.

def select(request):
    return render(request, 'select.html')
    #if request.method == ""