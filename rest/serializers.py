from rest_framework import serializers
from django.conf import settings
from  django.db.models import fields
from  .models import *

class BoardSerializer(serializers.ModelSerializer):
    boards = serializers.StringRelatedField(many=True)
    class Meta:
        model = Board
        fields = ['name', 'color', 'created_at', 'updated_at', 'boards']

class PanelSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board, required=False, source='board.name')
    card = serializers.StringRelatedField(many=True)
    created_by = serializers.StringRelatedField(many=False) # source='created_by.id')
    class Meta:
        model = Card
        fields = ['id', 'name', 'color', 'created_at', 'updated_at', 'card', 'created_by', 'board']
        depth = 3

