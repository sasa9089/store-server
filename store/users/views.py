from django.shortcuts import render, HttpResponsePermanentRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponsePermanentRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    contex = {'form': form}
    return render(request, 'users/login.html', contex)


def registration(request):
    return render(request, 'users/registration.html')
