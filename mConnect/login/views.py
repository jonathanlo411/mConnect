from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Form import
from .forms import log_in

def login_vw(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/animelist/')
        return render(request, "login/login_error.html", {'login': log_in})

    context = {
        'login': log_in
    }
    return render(request, "login/login.html", context)