from .models import Review
from rest_framework import viewsets
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, permissions


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]
