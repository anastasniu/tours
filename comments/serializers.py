from .models import Review
from rest_framework import serializers



class ReviewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields =['id', 'tours', 'name', 'body']

        


    