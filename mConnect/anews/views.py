from django.shortcuts import render

# Create your views here.

# Brining in models
from .models import NewsEntrys

def anews(request):
    news = ""
    context = {
        'news': news
    }
    return render(request, "anews/anews.html", context)

# Obtaining news source
def pullnews():
    """
    Pulls the news information from AnimeNewsNetworl via XML and saves to database
    """
    news_entry = NewsEntrys(
        title = '',
        date = '',
        desc = '',
        category = ''
    )
    news_entry.save()
