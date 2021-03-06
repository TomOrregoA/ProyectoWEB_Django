from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Obra
from .serializers import ObraSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_obras(request):
    """

    Lista todas las obras
    """
    if request.method == 'GET':
        obra = Obra.objects.all()
        serializer = ObraSerializer(obra, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ObraSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_obra(request, title):
    """

    GET, UPDATE, o DELETE de una obra en particular
    """
    try:
        obra = Obra.objects.get(title = title)
    except Obra.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ObraSerializer(obra)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ObraSerializer(obra, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        obra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)