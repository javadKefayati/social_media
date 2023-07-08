from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from django.core.validators import MinLengthValidator
from social_media.users.models import BaseUser 
from social_media.profile.models import Profile
from social_media.api.mixins import ApiAuthMixin
from social_media.profile.selectors import get_profile
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from drf_spectacular.utils import extend_schema


class ProfileApi(ApiAuthMixin, APIView):

    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile 
            fields = ("user","bio", "posts_count", "follower_count", "following_count")

    @extend_schema(responses=OutPutSerializer)
    def get(self, request):
        query = get_profile(user=request.user)
        return Response(self.OutPutSerializer(query, context={"request":request}).data)