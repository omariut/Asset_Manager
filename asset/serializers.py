from rest_framework.serializers import ModelSerializer
from asset.models import Asset,Category,HandOverOrReturn

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AssetSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class HandOverOrReturnSerializer(ModelSerializer):
    class Meta:
        model = HandOverOrReturn
        fields = '__all__'