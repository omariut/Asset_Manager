from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


User = get_user_model()

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'is_active': {'read_only': True}, 'is_superuser': {'read_only': True}, 'is_staff': {'read_only': True}, 'verified': {'read_only': True}}
        exclude = ('password', 'groups', 'user_permissions')



class UserProfileLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'address', 'contact_number', 'customer_type')

