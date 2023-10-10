from django.test import TestCase
from django.shortcuts import render

def home(request):
    return render(request, "project/index.html")
