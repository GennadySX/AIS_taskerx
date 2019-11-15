from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from ais.models import *


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['type', 'task', 'text', 'status']


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['type', 'task', 'text', 'file']


def add_task(request):
    form = TaskModelForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/tasks/')
    return render(request, 'ais/add_task.html', {'form': form})


def task(request):
    submitted = False
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/task?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True
    tasks = Task.objects.all()
    return render(request, 'task/index.html', {'form': form, 'tasks': tasks})


def change_task(request, id):
    t = Task.objects.get(pk=id)
    if request.method == "POST":
        form = TaskModelForm(request.POST, request.FILES, instance=t)
        if form.is_valid():
            form.save()
            return redirect('/tasks/')
    else:
        form = TaskModelForm(instance=t)
    return render(request, 'ais/add_task.html', {'form': form})


class AdvantagesForm(forms.ModelForm):
    class Meta:
        model = Advantage
        fields = ('username', 'name', 'about', 'task', 'see')





class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('username', 'user', 'feedback', 'advantage')
