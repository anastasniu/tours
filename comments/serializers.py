from .models import Review, Rating
from rest_framework import serializers
from django.db.models import Avg


class RatingSerializer(serializers.ModelSerializer):
    new_rating = serializers.IntegerField(write_only=True)

    class Meta:
        model = Rating
        fields = '__all__'

    def validate_new_rating(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError("Рейтинг должен быть от 0 до 5")
        return value

    def update(self, instance, validated_data):
        new_rating = validated_data.pop('new_rating', None)
        if new_rating is not None:
            instance.rating = new_rating
            instance.save()
        return instance

    def get_average_rating(self, obj):
        ratings = Rating.objects.filter(course=obj)
        if ratings.exists():
            average = ratings.aggregate(Avg('rating')).get('rating__avg')
            return round(average, 1)
        return None


class ReviewSerializer(serializers.ModelSerializer):
    tours = serializers.StringRelatedField()
    name = serializers.StringRelatedField()
    rating = RatingSerializer()

    class Meta:
        model = Review
        fields =['id', 'tours', 'name', 'body', 'rating']
    
    def create(self, validated_data):
        rating_data = validated_data.pop('rating')
        review = Review.objects.create(**validated_data)
        Rating.objects.create(review=review, **rating_data)
        return review







      