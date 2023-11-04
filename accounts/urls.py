from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    
]

