from django.contrib import admin
from django.urls import path
from asset.views import (
    CategoryListCreateAPIView,
    CategoryRetrieveAPIView,
    AssetListCreateAPIView,
    AssetRetrieveUpdateDestroyAPIView,
    HandOverOrReturnListCreateAPIView,
    HandOverOrReturnRetrieveUpdateDestroyAPIView,
    HandOverHistoryAPIView
)

urlpatterns = [
    path(
        "categories/", CategoryListCreateAPIView.as_view(), name="list-create-category"
    ),
    path(
        "categories/<int:pk>",
        CategoryRetrieveAPIView.as_view(),
        name="retrieve-update-category",
    ),
    path("", AssetListCreateAPIView.as_view(), name="list-create-asset"),
    path(
        "<int:pk>",
        AssetRetrieveUpdateDestroyAPIView.as_view(),
        name="retrieve-update-asset",
    ),
    path(
        "handovers/",
        HandOverOrReturnListCreateAPIView.as_view(),
        name="list-create-handover",
    ),
    path(
        "handovers/<int:pk>",
        HandOverOrReturnRetrieveUpdateDestroyAPIView().as_view(),
        name="retrieve-update-handover",
    ),

    path(
        "history/<int:pk>",
        HandOverHistoryAPIView.as_view(),
        name="asset-history",
    ),
]
