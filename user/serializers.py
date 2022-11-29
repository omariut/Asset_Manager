from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


User = get_user_model()



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'password':{'write_only':True}, 'is_active': {'read_only': True}, 'is_superuser': {'read_only': True}, 'is_staff': {'read_only': True}, 'verified': {'read_only': True}, 'store': {'read_only': True}}
        exclude = ('groups', 'user_permissions')

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)




