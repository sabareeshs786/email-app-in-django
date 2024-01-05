from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

# Create your views here.
def inbox(request):
    
    return render(request, "features/index.html")