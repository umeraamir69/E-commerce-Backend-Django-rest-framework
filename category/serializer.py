from rest_framework import serializers
from . import models



class categorySerializer(serializers.ModelSerializer):

    class Meta :
        model = models.Category
        exclude = ['description' , 'is_active']
        # fields = ['id' , 'name', 'slug', 'is_active' ,'is_featured' , 'image']



