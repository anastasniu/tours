from .models import Tour
from .serializers import ToursSerializer, ToursCreateSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 
from .permissions import IsOwnerOrReadOnly



class TourAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = ToursSerializer


class TourAPICreate(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = ToursCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class TourAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = ToursSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)