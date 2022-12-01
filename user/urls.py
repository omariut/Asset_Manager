from django.urls import path
from user.views import (
    registration, 
    login, 

)
urlpatterns = [
    path('', registration, name='user-registration-api'),
    path('login', login, name='user-login-api'),


]