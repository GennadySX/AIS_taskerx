from django.contrib import admin
from django.contrib.auth.views import LoginView

from django.urls import path, include
from ais.views import *
from ais import forms as task

urlpatterns = [
    path('', aisView.index),
    path('advantages/', aisView.advantages),
    path('task/', task.add_task, name='task'),
    path('tasks/', task.task, name='task'),
    path('login/',  aisView.login),
    path('logout/',  aisView.logout),
    path('signup/',  aisView.signup),

]

