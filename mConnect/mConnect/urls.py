from django.contrib import admin
from django.urls import path

#pages
from landing.views import landing, about
from animelist.views import animelist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name="landing"),
    path('about', about, name="about"),
    path('animelist/', animelist, name='animelist')
]
