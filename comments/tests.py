from django.test import TestCase
from comments import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('',views.ReviewList,basename='')

urlpatterns = []

urlpatterns +=router.urls