from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('',views.ToursList,basename='')

urlpatterns = [
    path('list/', views.TourAPIView.as_view()),
]


urlpatterns +=router.urls

