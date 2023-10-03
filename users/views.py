from django.shortcuts import render
from django.contrib.auth import login ,logout,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request , "users/login.html")
    return render(request , "users/user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request , user)
            return render(request , "users/user.html")
        else:
            return render(request , "users/login.html" , {
                "message" : "Invalid Logging"
            })
    return HttpResponseRedirect(reverse("index"))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))