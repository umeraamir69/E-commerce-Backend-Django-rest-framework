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
                req_featuer = request.query_params.get('featuer')
                req_orderings = request.query_params.get('ordering')
                if req_featuer is not None:
                    categories = categories.filter(is_featured=req_featuer.capitalize())
                    print ("i am here")
                if req_orderings is not None :
                    categories = categories.order_by(req_orderings)
                serializerCategory=  serializer.categorySerializer(categories , many = True)
                return Response(serializerCategory.data , status.HTTP_200_OK)
        elif request.method =='POST':
            serializerCat = serializer.CategorySerializer(data=request.data)
            if serializerCat.is_valid():
                serializerCar.save() 
                return Response(serializerCar.data, status=status.HTTP_201_CREATED)
            return Response(serializerCar.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print (e)
        return Response({'detail': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def getCategoryById(request , id):
    try :
        category = get_object_or_404(models.Category, Q(pk =id) & Q(is_active = True)  )
        searilzerCategory = serializer.categorySerializer(category)
        return Response(searilzerCategory.data , status.HTTP_200_OK)
    except Http404:
        return Response({'detail': 'No Category Found'} ,status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def getCategoryBySlug(request , slug):
    try :
        category = get_object_or_404(models.Category, Q(slug = slug) & Q(is_active = True)  )
        searilzerCategory = serializer.categorySerializer(category)
        return Response(searilzerCategory.data , status.HTTP_200_OK)
    except Http404:
        return Response({'detail': 'No Category Found'} ,status.HTTP_404_NOT_FOUND)


