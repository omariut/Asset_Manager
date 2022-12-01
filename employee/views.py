from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework import status

from base.utils import identifier_builder

from employee.models import Employee
from employee.serializers import EmployeeSerializer
class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter()

    def create(self, request):
        request.data["employee_id"]=identifier_builder(table_name='employees', prefix="EMPL-")
        request.data["created_by"]=request.user.id
        return super().create(request)

class EmployeeRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter()

    def patch(self, request):
        request.data.pop("employee_id")