from django.urls import path
from .views import CustomerView, CustomerDetailView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('customer/', CustomerView.as_view(), name='customer'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('api-token-auth/', views.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]