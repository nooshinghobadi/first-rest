from rest_framework import serializers
from .models import Todo

#class TodoSerializer(serializers.Serializer):

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        #fields = ['title','id','content']
        fields = '__all__'
