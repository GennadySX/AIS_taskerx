from rest_framework import serializers
from django.conf import settings
from  django.db.models import fields
from  .models import *

class BoardSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    color = serializers.CharField()
    created_at = serializers.DateField()
    updated_at = serializers.DateField()
    created_by_id = serializers.IntegerField()
    def create(self, validated_data):
        return Board.objects.create(**validated_data)
    class Meta:
        model = Board
        fields = ['name', 'color', 'created_at', 'updated_at', 'created_by_id']

class PanelCRUDSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    color = serializers.CharField()
    created_at = serializers.DateField()
    updated_at = serializers.DateField()
    board_id = serializers.IntegerField()
    created_by_id = serializers.IntegerField()
    def create(self, validated_data):
        return Panel.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     return  Panel.objects.update(**validated_data)
    class Meta:
        model = Panel
        fields = ['name', 'color', 'created_at', 'updated_at', 'board_id', 'created_by_id']

class PanelSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board, required=False, source='board.name')
    card = serializers.StringRelatedField(many=True)
    created_by_id = serializers.StringRelatedField(many=False)  # source='created_by.id')
    class Meta:
        model = Card
        fields = ['id', 'name', 'color', 'created_at', 'updated_at', 'card', 'created_by_id', 'board']
        depth = 3

