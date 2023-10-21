from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def class9(request):
    return render(request, "class9.html")


def class10(request):
    return render(request, "class10.html")
