from django.contrib import admin
from django.urls import path
from company.views import CompanyListCreateAPIView,CompanyRetrieveUpdateAPIView
urlpatterns = [
    path('',CompanyListCreateAPIView.as_view(),name='list-create-company'),
    path('<int:pk>',CompanyRetrieveUpdateAPIView.as_view(),name='retrieve-update-company'),

]