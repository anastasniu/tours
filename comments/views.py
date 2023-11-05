from .models import Review
from rest_framework import permissions,viewsets
from .serializers import ReviewsSerializer



class ReviewList(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewsSerializer