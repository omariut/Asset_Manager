from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.core.exceptions import BadRequest
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status

from asset.models import Asset, Category, HandOverOrReturn
from asset.serializers import (
    CategorySerializer,
    AssetSerializer,
    HandOverOrReturnSerializer,
)

import datetime


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()

    def create(self, request):
        request.data["created_by"] = request.user.id
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
        request.data["created_by"] = request.user.id
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
        condition = self.request.data.get("condition")
        with transaction.atomic():
            handover = serializer.save()
            asset = handover.asset

            # swap asset
            if asset.belongs_to == "admin":
                asset.belongs_to = "employee"
                handover.transfer_to = "employee"
            else:
                asset.belongs_to = "admin"
                handover.transfer_to = "admin"
                handover.return_date = None
            handover.save()

            # update asset condition
            asset.condition = condition
            asset.save()

    def create(self, request):
        return_date = datetime.datetime.strptime(
            request.data.get("return_date"), "%Y-%m-%d"
        ).date()
        handover_date = datetime.datetime.strptime(
            request.data.get("handover_date"), "%Y-%m-%d"
        ).date()

        last_handover = HandOverOrReturn.objects.filter().latest("handover_date")

        if handover_date < last_handover.handover_date:
            raise BadRequest("Invalid Handover Date")

        if return_date and (return_date < handover_date):
            raise BadRequest("Invalid Return Date")
        request.data["created_by"] = request.user.id
        return super().create(request)


class HandOverOrReturnRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = (IsAuthenticated,)
    serializer_class = HandOverOrReturnSerializer
    queryset = HandOverOrReturn.objects.filter()


class HandOverHistoryAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = HandOverOrReturnSerializer

    def get_queryset(self):
        asset_id = self.kwargs.get("pk")
        return HandOverOrReturn.objects.filter(asset_id=asset_id).order_by(
            "-handover_date", "-id"
        )
