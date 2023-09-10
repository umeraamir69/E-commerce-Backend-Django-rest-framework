from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializer

from . import models

# Create your views here.

@api_view(['GET', 'POST'])
def category (request):
    if request.method =='GET':
            categories = models.Category.objects.filter(is_active= True)
            serializerCategory=  serializer.categorySerializer(categories , many = True)
            return Response(serializerCategory.data , status.HTTP_200_OK)
    elif request.method =='POST':
        serializerCat = serializer.CategorySerializer(data=request.data)
        if serializerCat.is_valid():
            serializerCar.save() 
            return Response(serializerCar.data, status=status.HTTP_201_CREATED)
        return Response(serializerCar.errors, status=status.HTTP_400_BAD_REQUEST)