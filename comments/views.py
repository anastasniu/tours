from .models import Review
from rest_framework import viewsets
from .serializers import ReviewsSerializer
from rest_framework.permissions import IsAuthenticated



class ReviewList(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewsSerializer
    permission_classes = [IsAuthenticated]
