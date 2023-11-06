from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import User
from django.contrib.auth import authenticate

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length = 80)
    username = serializers.CharField(max_length = 45)
    password = serializers.CharField(min_length = 8, write_only = True)
    
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("Email has already been used")
        return super().validate(attrs)


    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attr):
        self.token = attr['refresh']
        return attr
    
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad token')

        


