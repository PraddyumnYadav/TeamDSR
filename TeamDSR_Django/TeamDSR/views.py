from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def class9(request):
    notes = [
        {
            "name": "The French Revolution",
            "pdf": "PDFs/Class 9th/The French Revolution one shot revision.pdf",
            "thumbnail": "Images/class9/the_french_revolution.webp"
        },
    ]
    return render(request, "class9.html", context=notes[0])


def class10(request):
    return render(request, "class10.html")
