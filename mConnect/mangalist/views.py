from django.shortcuts import render

# Create your views here.


def mangalist(request):
    return render(request, 'mangalist/mangalist.html')