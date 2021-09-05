from django.contrib import admin
from django.urls import path
from landing.views import landing, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name="landing"),
    path('about', about, name="about")
]
