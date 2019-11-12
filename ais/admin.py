from django.contrib import admin
from .models import *
# Register your models here.

from django.contrib.admin import AdminSite


class TaskAdmin(admin.ModelAdmin):
    list_display = ['task', 'status']


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskFiles)
admin.site.register(Advantage)
admin.site.register(Feedback)


