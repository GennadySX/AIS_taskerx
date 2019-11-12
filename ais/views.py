from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.
from ais.forms import *
import random


class aisView:
    def index(request):
        adv = Advantage.objects.all().order_by('id').reverse()
        return render(request, 'main/index.html', {'adv_list': adv})

    def login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect('/admin/')
            else:
                mess = "Логин или пароль неверные!"
                return render(request, 'auth/index.html', {'mess': mess})
        return render(request, 'auth/index.html')

    def logout(request):
        auth.logout(request)
        return HttpResponseRedirect('/')

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
                auth.login(request, user)
                return HttpResponseRedirect('/admin/')
        else:
            form = UserCreationForm()
        return render(request, 'auth/signUp.html', {'form': form})

    def advantages(request):
        adv = Advantage.objects.all().order_by('id').reverse()
        return render(request, 'main/advantages/advantage.html', {'adv_list': adv})

    def advantage_byId(request, adv_id):
        if request.method == 'POST':
            form = FeedbackForm(request.POST or None)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        adv = Advantage.objects.filter(id=adv_id).get()
        feedbacks = Feedback.objects.all().filter(advantage=adv_id)
        see = random.randint(0, 100)
        return render(request, 'main/advantages/element.html', {'adv': adv, 'see': see, 'comments': feedbacks, "count_feed": feedbacks.count()})

    def advantageCreate(request):
        if request.method == 'POST':
            form = AdvantagesForm(request.POST or None)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/advantages')
            else:
                return HttpResponse(form, content_type='application/json')
        tasks = Task.objects.all()
        return render(request, 'main/advantages/create.html', {'tasks': tasks})

    def feedback(request):
        if request.method == 'POST':
            form = FeedbackForm(request.POST or None)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                return HttpResponse(form, content_type='application/json')
        tasks = Task.objects.all()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
