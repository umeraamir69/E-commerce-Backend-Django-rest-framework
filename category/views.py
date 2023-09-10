from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from . import serializer
from django.shortcuts import get_object_or_404
from django.http import Http404
from . import models

# Create your views here.

@api_view(['GET', 'POST'])
def category (request):
    try:
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
    except Exception as e:
        return Response({'detail': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def getCategoryById(request , id):
    try :
        category = get_object_or_404(models.Category, Q(pk =id) & Q(is_active = True)  )
        searilzerCategory = serializer.categorySerializer(category)
        return Response(searilzerCategory.data , status.HTTP_200_OK)
    except Http404:
        return Response([] ,status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def getCategoryBySlug(request , slug):
    try :
        category = get_object_or_404(models.Category, Q(slug = slug) & Q(is_active = True)  )
        searilzerCategory = serializer.categorySerializer(category)
        return Response(searilzerCategory.data , status.HTTP_200_OK)
    except Http404:
        return Response([] ,status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getFeature(request):
    try :
        category = models.Category.objects.filter(is_featured= True)
        if category:
            searilzerCategory = serializer.categorySerializer(category , many=True)
            return Response(searilzerCategory.data , status.HTTP_200_OK)
        else:
            return Response({'detail': 'No featured categories found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
