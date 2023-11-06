from django.test import TestCase
<<<<<<< HEAD

# Create your tests here.
=======
from comments import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('',views.ReviewList,basename='')

urlpatterns = []

urlpatterns +=router.urls
>>>>>>> c21bb4f
