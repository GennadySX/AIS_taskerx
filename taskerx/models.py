from django.db import models
from django_mysql.models import EnumField
from django_enumfield import enum




# Create your models here.
class Cards(models.Model):
    name = models.CharField(max_length=255)
    priority = EnumField(choices=[0,1,2,3], default= 1)
    status = EnumField(choices=[0,1,2,3], default= 1)
    desc = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.name


class Panels(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.IntegerField()
    color = models.CharField(max_length=50)
    creator_id = models.IntegerField()
    desc = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.name


class PanelUsers(models.Model):
    user_id = models.IntegerField()
    panel_id = models.IntegerField()
    created_at = models.DateField(auto_now=True)
    def __str__(self):
        return  self.name

class CardUser(models.Model):
    manager_id = models.IntegerField()
    perfomer_id = models.IntegerField()
    card_id = models.IntegerField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.card_id