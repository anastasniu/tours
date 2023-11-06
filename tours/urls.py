from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TourAPIView.as_view()),
<<<<<<< HEAD
    path('create/<int:pk>/', views.TourAPICreate.as_view()),
    path('update/<int:pk>/', views.TourAPIUpdateDestroy.as_view()),
=======
    path('tour/<int:pk>', views.TourAPIView.as_view()),
    path('create/', views.TourAPICreate.as_view()),
    path('update/<int:pk>/', views.TourAPIUpdateDestroy.as_view()),

>>>>>>> c21bb4f
]