
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.core.exceptions import BadRequest
from django.db import transaction
from rest_framework import status

from asset.models import Asset,Category,HandOverOrReturn
from asset.serializers import CategorySerializer,AssetSerializer,HandOverOrReturnSerializer
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()

    def create(self, request):
        request.data["created_by"]=request.user.id
        return super().create(request)

class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()
class AssetListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AssetSerializer
    queryset = Asset.objects.filter()

    def create(self, request):
        request.data["created_by"]=request.user.id
        return super().create(request)

class AssetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AssetSerializer
    queryset = Asset.objects.filter()


class HandOverOrReturnListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = HandOverOrReturnSerializer
    queryset = HandOverOrReturn.objects.filter()

    def perform_create(self, serializer):
        condition=self.request.data.get("condition")
        with transaction.atomic():
            handover=serializer.save()
            asset=handover.asset
            if asset.belongs_to=='admin':
                asset.belongs_to='employee'
            else:
                asset.belongs_to='admin'
            asset.condition=condition
            asset.save()
            

    def create(self, request):
        request.data["created_by"]=request.user.id
        return super().create(request)

class HandOverOrReturnRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = HandOverOrReturnSerializer
    queryset = HandOverOrReturn.objects.filter()