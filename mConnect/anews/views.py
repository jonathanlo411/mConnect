from django.shortcuts import render

# Create your views here.


def anews(request):
    return render(request, "anews/anews.html")