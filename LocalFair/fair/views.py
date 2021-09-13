import urllib.parse

from django.shortcuts import render
from rest_framework import routers, viewsets, generics, filters
from django.contrib.auth.models import User
from .serializers import UserSerializer, DichSerialazer, Dich2Serialazer, ProductSerializer
from .models import Dich, Dich2, Product
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import django_filters.rest_framework
import re


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DichViewSet(viewsets.ModelViewSet):
    serializer_class = DichSerialazer
    queryset = Dich.objects.all()

class Dich2ViewSet(viewsets.ModelViewSet):
    serializer_class = Dich2Serialazer
    queryset = Dich2.objects.all()

@csrf_exempt
def dich_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        dich = Dich.objects.all()
        serializer = DichSerialazer(dich, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DichSerialazer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ProductsViewSet(viewsets.ViewSet):
    def list(self, request):
        data = urllib.parse.unquote(request.get_full_path())
        dict_url = dict(param.split("=") for param in data.split('?')[1].split("&"))

        queryset = Product.objects.filter(**dict_url)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet2(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["category", 'title']

# https://www.django-rest-framework.org/api-guide/filtering/