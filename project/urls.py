from django.urls import path
from .views import UserCreateAPIView, UsersAPIView, UserAPIView, UserUpdateAPIView, UserDeleteAPIView


urlpatterns = [
    path('users/', UsersAPIView.as_view()),
    path('user/<int:pk>/', UserAPIView.as_view()),
    path('user-create/', UserCreateAPIView.as_view()),
    path('user-update/<int:pk>/', UserUpdateAPIView.as_view()),
    path('user-delete/<int:pk>/', UserDeleteAPIView.as_view())
]