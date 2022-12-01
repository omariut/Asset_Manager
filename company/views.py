from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework import status

from company.models import Company
from company.serializers import CompanySerializer
class CompanyListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer
    queryset = Company.objects.filter()

    def create(self, request):
        request.data["created_by"]=request.user.id
        return super().create(request)

class CompanyRetrieveUpdateAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer
    queryset = Company.objects.filter()