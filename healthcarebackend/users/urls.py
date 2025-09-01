from django.contrib import admin
from django.urls import path, include
from .views import UserRegisteration, UserLoginView, UserProfileView

urlpatterns = [
    path('register/', UserRegisteration.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
