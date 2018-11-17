from django.shortcuts import render
from .models import *
# Create your views here.

def select(request):
    return render(request, 'select_paul.html')
    #if request.method == ""