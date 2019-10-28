from django.db import models
from django.conf import settings
from django.utils import timezone
from enum import Enum
from django.utils.translation import gettext as _
from django.core.validators import MaxLengthValidator, MinValueValidator
# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=155)
    color = models.CharField(max_length=155, null=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner_board', on_delete=models.CASCADE)
    created_at =  models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)


class Panel(models.Model):
    board = models.ForeignKey(Board, related_name='boards', on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    color = models.CharField(max_length=155, null=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner_panel', on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    def __str__(self):
        return '%s: %s' % (self.name, self.color)


class Card(models.Model):

    STATUS_TASK = (
        (0, 'unactive'),
        (1, 'active'),
        (2, 'inprogress'),
        (3, 'finish'),
        (4, 'deadline')
    )
    panel = models.ForeignKey(Panel, related_name='card', on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    desc = models.TextField()
    status = models.IntegerField(choices= STATUS_TASK, default=STATUS_TASK[0])
    color = models.CharField(max_length=155, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner_card', on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

# class CheckBox(models.Model):
#     STATUS_CHECK = (
#         (0, 'unchecked'),
#         (1, 'checked'),
#     )
#     name = models.CharField(max_length=255)
#     desc = models.TextField()
#     status = models.IntegerField(choices=STATUS_CHECK, default=STATUS_CHECK[0])
#     created_at = models.DateField(timezone.now())
#     updated_at = models.DateField(timezone.now())
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users', on_delete=models.CASCADE)
#
# class FileTask(models.Model):
#     # это чтобы определить отображение файла
#     TYPE_FILE = (
#         (0, 'image'),
#         (1, 'doc'),
#     )
#     # тип карты
#
#     TYPE_ITEM = (
#         (0, 'board'),
#         (1, 'panel'),
#         (2, 'card'),
#     )
#     # тип использования
#     TYPE_USE = (
#         (0, 'background'),
#         (1, 'file'),
#     )
#
#     path = models.CharField(max_length=255)
#     filename = models.CharField(max_length=255)
#     type = models.IntegerField(null=True)
#     type_file = models.CharField(max_length=255, choices=TYPE_FILE, default=TYPE_FILE[0])
#     item_type = models.IntegerField(choices=TYPE_ITEM, default=TYPE_ITEM[0])
#     use_type = models.IntegerField(choices=TYPE_USE, default=TYPE_USE[0])
#     item_id = models.IntegerField()
#
#
# class ReplyTask(models.Model):
#     item_id = models.IntegerField()
#     text = models.TextField()
#     file = models.ForeignKey(FileTask, on_delete=models.CASCADE)
#
