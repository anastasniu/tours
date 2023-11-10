from rest_framework import serializers
from .models import Tour
from comments.models import Review
from comments.serializers import ReviewSerializer



class ToursListSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        
        model = Tour
        fields = ['title', 'city', 'address', 'distance', 'price', 'maxGroupSize','desc', 'reviews', 'photo', 'featured' ]
        

        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        field_value = data.get('address')

        if field_value is None:
            data.pop('address')
            
        return data


class ToursSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tour
        fields = ('title', 'city', 'address', 'distance', 'price', 'maxGroupSize', 'desc', 'photo', 'featured')


    def create(self, validated_data):
        user = self.context['request'].user
        tour = Tour.objects.create(user=user, **validated_data)
        return tour
