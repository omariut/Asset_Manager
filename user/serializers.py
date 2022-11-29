from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


User = get_user_model()


class UserLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'contact_number', 'is_active', 'customer_type')


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    store = SerializerMethodField()

    def get_store(self, obj):
        if obj.store:
            return {
                'slug' : obj.store.slug,
                'name' : obj.store.name
            }
        else:
            return None
    class Meta:
        model = User
        extra_kwargs = {'is_active': {'read_only': True}, 'is_superuser': {'read_only': True}, 'is_staff': {'read_only': True}, 'verified': {'read_only': True}, 'store': {'read_only': True}}
        exclude = ('password', 'groups', 'user_permissions')



class CustomerSerializer(serializers.ModelSerializer):
    previous_due = serializers.FloatField(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'contact_number', 'address', 'is_active', 'previous_due', 'customer_type')


class CustomerLiteSerializer(serializers.ModelSerializer):
    previous_due = SerializerMethodField()

    def get_previous_due(self, obj):
        return obj.order_set.aggregate(Sum('due_amount')).get('due_amount__sum')
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'contact_number', 'address', 'is_active', 'previous_due', 'customer_type')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'




class UserProfileLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'address', 'contact_number', 'customer_type')

