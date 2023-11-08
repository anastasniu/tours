from .models import Profile
from rest_framework import generics
# from rest_framework import viewsets
from .serializers import ProfileSerializer
# from rest_framework.permissions import IsAdminUser


class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer