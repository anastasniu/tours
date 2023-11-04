from rest_framework import serializers
from tours.models import Tour

class ToursSerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField()
    class Meta:
        model = Tour
        fields = '__all__'