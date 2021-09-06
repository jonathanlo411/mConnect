from django.contrib import admin
from django.urls import path

#pages
from landing.views import landing, about
from animelist.views import animelist
from login.views import login_vw
from signup.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name="landing"),
    path('about', about, name="about"),
    path('animelist/', animelist, name='animelist'),
    path('login/', login_vw, name="login"),
    path('signup/', signup, name="signup")
]
