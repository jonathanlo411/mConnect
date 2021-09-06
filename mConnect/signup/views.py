from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Forms and Models
from .forms import UserCreation
from .models import userprofile

def signup(request):
    if request.method == 'POST':
        user_form = UserCreation(data=request.POST)
        if user_form.is_valid():
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            if User.objects.filter(email = email).exists():
                return render(request,'signup/signup_error.html', {"ucreation": UserCreation, "error": "Email Already Exists!"})
            if User.objects.filter(username = username).exists():
                return render(request,'signup/signup_error.html', {"ucreation": UserCreation, "error": "Username Already Exists!"})
            else:
                # saving user for login info
                user = User.objects.create_user(email=email, username=username, password=password)
                user.set_password(password)
                user.save()
                # creating a userprofile
                userp = userprofile(email = email, username = username, password = password)
                userp.save()
                u = User.objects.get(email=email)
                user = authenticate(username=u.get_username(),password=password)
                login(request, user)
                return HttpResponseRedirect('/animelist/')
    else:
        form = UserCreation()

    context = {
        "ucreation": UserCreation
    }
    return render(request, "signup/signup.html", context)