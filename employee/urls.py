from django.contrib import admin
from django.urls import path
from employee.views import EmployeeListCreateAPIView,EmployeeRetrieveUpdateAPIView

urlpatterns = [
    path('',EmployeeListCreateAPIView.as_view(), name='list-create-employee'),
    path('<int:pk>',EmployeeRetrieveUpdateAPIView.as_view(),name='retrieve-update-employee'),

]