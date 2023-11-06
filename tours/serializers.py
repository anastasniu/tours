from rest_framework import serializers
from tours.models import Tour
from comments.models import Review
from comments.serializers import ReviewsSerializer



class ToursListSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    reviews = ReviewsSerializer(many=True, read_only=True)

    class Meta:
        
        model = Tour
        fields = ['id','title', 'city', 'address', 'distance', 'price', 'maxGroupSize','desc', 'reviews', 'photo', 'featured' ]
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        field_value = data.get('address')

        if field_value is None:
            data.pop('address')
            
        return data


class ToursSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tour
        fields =['id','title', 'city', 'address', 'distance', 'price', 'maxGroupSize','desc', 'photo']
