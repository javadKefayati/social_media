from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from django.core.validators import MinLengthValidator
from .validators import number_validator, special_char_validator, letter_validator
from social_media.users.models import BaseUser , Profile
from social_media.api.mixins import ApiAuthMixin

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from drf_spectacular.utils import extend_schema


class PostView(APIView, ApiAuthMixin):
    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile 
            fields = ("id","text","crated_at","updated_at")

    
    @extend_schema(Response= OutPutSerializer)
    def get(request, post_id:int):
        ...
    
    def post(request):
        ...

