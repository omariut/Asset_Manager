from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from user.views import (
    registration, 
    login, 

)
urlpatterns = [
    path('', registration, name='user-registration-api'),
    path('/login', login, name='user-login-api'),


]