from .models import Tour
<<<<<<< HEAD
<<<<<<< HEAD
from .serializers import ToursSerializer
=======
from .serializers import ToursSerializer, ToursCreateSerializer
>>>>>>> c21bb4f
=======
from .serializers import ToursListSerializer, ToursSerializer
>>>>>>> 31d1881
from rest_framework import generics
from rest_framework import viewsets
from .serializers import ToursSerializer
from rest_framework.permissions import IsAdminUser


class TourAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = ToursListSerializer


<<<<<<< HEAD
class TourAPICreate(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
<<<<<<< HEAD
    serializer_class = ToursSerializer
    permission_classes = (IsAuthenticatedOrReadOnly)
=======
    serializer_class = ToursCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
>>>>>>> c21bb4f


class TourAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = ToursSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
=======
class ToursList(viewsets.ModelViewSet):
    queryset=Tour.objects.all()
    serializer_class=ToursSerializer
    permission_classes = [IsAdminUser]

>>>>>>> 31d1881
