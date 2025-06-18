from rest_framework import serializers
from .models import *

class CommnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ='__all__'

# this is how you perform nested serializers
class BlogSerializer(serializers.ModelSerializer):
    comments =  CommnetSerializer(many=True,read_only=True)
    class Meta:
        model = Blog
        fields ='__all__'
    