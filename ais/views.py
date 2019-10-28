from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.
from ais.forms import *


class aisView:
    def index(request):
        return render(request, 'dashboard/index.html')

    def login(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/admin/')
        return render(request, 'auth/index.html')

    def signup(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password1']
                )
                user.is_staff = True
                user.is_superuser = True
                user.save()
                # Login the user
                login(request, user)
                return HttpResponseRedirect('/admin/')
        else:
            form = UserCreationForm()
        return render(request, 'auth/signUp.html', {'form': form})
