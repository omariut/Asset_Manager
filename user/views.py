import json
import logging
import random
import jwt
import requests
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from user.helpers import create_tokens
from user.models import User
from user.serializers import UserSerializer, UserTokenSerializer
from user.utils import delete_cache, get_cache, set_cache

logger = logging.getLogger('django')
class UnprocessableEntity(APIException):
    status_code = 406
    default_code = 406
    default_detail = 'unprocessable entity'

@api_view(['POST'])
@permission_classes([AllowAny])
def registration(request: Request) -> Response:
    username = request.data.get('username')
    try:
        User.objects.get(username=username)
        raise UnprocessableEntity(
            detail='username already exists', code=status.HTTP_406_NOT_ACCEPTABLE)
    except User.DoesNotExist:
        user = User()
        user.username = username
        user.set_password(raw_password=request.data.get('password'))
        user.verified = True
        user.profile_pic_url = request.data.get('profile_pic_url')
        user.address = request.data.get('address')
        user.gender = request.data.get('gender', 'male')
        user.is_staff = request.data.get('is_staff', False)
        user.first_name = request.data.get('first_name')
        user.last_name = request.data.get('last_name')
        user.contact_number = request.data.get('username')
        if User.objects.filter(contact_number = user.contact_number).exists():
            raise UnprocessableEntity(
                detail='contact already exists', code=status.HTTP_406_NOT_ACCEPTABLE)
        user.save()
        return Response(data={'data': UserSerializer(user).data}, status=status.HTTP_201_CREATED)




@api_view(['POST'])
@permission_classes([AllowAny])
def login(request: Request) -> Response:
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        raise ValidationError(
            detail='username and password if required', code=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(username__exact=username)
        if not user.check_password(raw_password=password):
            raise ValidationError(detail='invalid password',
                                  code=status.HTTP_400_BAD_REQUEST)
        access_token, refresh_token = create_tokens(user=user)
        data = {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }
        set_cache(key=f'{username}_token_data', value=json.dumps(UserTokenSerializer(user).data), ttl=5*60*60)
        return Response(data=data, status=status.HTTP_201_CREATED)
    except User.DoesNotExist:
        raise ValidationError(detail='user not found',
                              code=status.HTTP_404_NOT_FOUND)




