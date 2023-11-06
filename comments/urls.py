from comments import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


<<<<<<< HEAD
router.register('/',views.ReviewList,basename='')
=======
router.register('',views.ReviewList,basename='')
>>>>>>> 31d1881

urlpatterns = []

urlpatterns +=router.urls