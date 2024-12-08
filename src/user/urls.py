from django.urls import path
from .views import  UsersView  ,user ,Users , sign_up
from .token import MyATokenObtainView
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/', UsersView.as_view(), name='users'),
    path('signup/', sign_up, name='signup'),
    path('user/<str:id>', user, name='users'),
    path('login/', MyATokenObtainView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]