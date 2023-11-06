from .models import Tour
from .serializers import ToursListSerializer, ToursSerializer
from rest_framework import generics
from rest_framework import viewsets
from .serializers import ToursSerializer
from rest_framework.permissions import IsAdminUser


class TourAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = ToursListSerializer


class ToursList(viewsets.ModelViewSet):
    queryset=Tour.objects.all()
    serializer_class=ToursSerializer
    permission_classes = [IsAdminUser]

