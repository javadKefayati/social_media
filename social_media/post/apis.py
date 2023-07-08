from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from social_media.users.models import BaseUser
from social_media.post.models import Post
from social_media.api.mixins import ApiAuthMixin

from .selectors import get_post

from drf_spectacular.utils import extend_schema


class PostApi(ApiAuthMixin,APIView):
    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post 
            fields = ("id", "text", "created_at", "updated_at")
            

    
    @extend_schema(responses= OutPutSerializer)
    def get(self, request, post_id:int):
        user = request.user
        post = get_post(user, post_id)
        if post.id is None:
            return Response({"msg":"post not found."})
        return Response(self.OutPutSerializer(post).data)
    
    
class AllPost(ApiAuthMixin,APIView):
    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post 
            fields = ("id", "text", "created_at", "updated_at")
            
    @extend_schema(responses= OutPutSerializer)
    def get(self, request, post_id:int):
        user = request.user
        
        return Response(self.OutPutSerializer(post, many=True).data)
        
        
    
