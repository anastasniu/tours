from rest_framework import serializers
from .models import Profile
from comments.models import Review


class UserProfileReviewSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    tours = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['id', 'tours', 'body', 'name']


class ProfileSerializer(serializers.ModelSerializer):
    user_profile_reviews = UserProfileReviewSerializer(many=True, source='name.user_review', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'name', 'avatar', 'bio', 'user_profile_reviews']


