from comments import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RatingViewSet

router = DefaultRouter()



router.register(r'ratings', RatingViewSet)


urlpatterns = [
    # path('api/', include(router.urls)),
]






# urlpatterns = [
#     path('reviews/<int:pk>/rate/', ReviewRatingUpdate.as_view(), name='review-rate'),
# ]

urlpatterns +=router.urls