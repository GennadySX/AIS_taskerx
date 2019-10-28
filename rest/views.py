from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import *
# Create your views here.
from .serializers import *

class BoardView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        board = Board.objects.all()
        serializer = BoardSerializer(board , many=True)
        return Response({'Panels': serializer.data, 'count': len(serializer.data)})
    def post(self, request):
        board = request.data.get('board')
        serializer = BoardSerializer(data=board)
        if serializer.is_valid(raise_exception=True):
            board_saved = serializer.save()
        return Response({'success': "Board created '{}' created successfully".format(board_saved.name)})

class PanelView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        panel = Panel.objects.all()
        serializer = PanelSerializer(panel, many=True)
        return Response({'Panels': serializer.data, 'count': len(serializer.data)})

    def post(self, request):
        panel = request.data.get('panel')
        serializer = PanelCRUDSerializer(data=panel)
        if serializer.is_valid(raise_exception=True):
            panel_saved = serializer.save()
        return Response({'success': "Panel created '{}' created successfully".format(panel_saved.name)})

class FrontView(APIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response({'boards': serializer.data})



