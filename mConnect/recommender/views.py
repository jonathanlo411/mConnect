from django.shortcuts import render

# Create your views here.


def recommender(request):
    return render(request, 'recommender/recommender.html')