from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from social_media.post.models import Post
from social_media.api.mixins import ApiAuthMixin
from .selectors import get_post
import django_filters
from drf_spectacular.utils import extend_schema, OpenApiParameter
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import mixins
from social_media.profile.selectors import get_profile
from rest_framework import permissions


from rest_framework import viewsets
        
# class PostList(         
#                 ApiAuthMixin,
#                 mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,
#                 generics.GenericAPIView,
#                 ):

#     class PostFilterSet(django_filters.FilterSet):
#         class Meta:
#             model = Post
#             fields = ['id','title']


#     class InputSerializer(serializers.Serializer):
#         title = serializers.CharField(max_length = 200)
#         content = serializers.CharField(max_length = 200)

#     class PostOutputSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Post
#             fields = ("id", "content", "title", "created_at", "updated_at")


#     serializer_class = PostOutputSerializer
#     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
#     filterset_class = PostFilterSet
#     model = Post
#     input_serializer_class = InputSerializer
    
#     def get_queryset(self):
#         user = self.request.user
#         posts = get_post(user = user)
#         return posts 
    
#     @extend_schema(responses=serializer_class,
#                     description="list posts",
#                     parameters=[
#                         OpenApiParameter(name='id', type=str, description='id of the post'),
#                         OpenApiParameter(name='title', type=str, description='Title of the post'),
#                         ],
#                     )
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
    
#     @extend_schema(request=input_serializer_class, responses=serializer_class, description="create post")
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
    
#     def perform_create(self, serializer):
#         user = self.request.user
#         title = serializer.data['title']
#         content = serializer.data['content']

#         profile = get_profile(user=user)
        
#         self.model(
#             profile=profile,
#             title=title,
#             content= content,
#         ).save() 
        
#     def create(self, request, *args,     **kwargs):
#         serializer = self.InputSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
class PostFilterSet(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['id', 'title']


class InputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=200)


class PostOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "content", "title", "created_at", "updated_at")


class PostList(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostOutputSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilterSet
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    Input_serializer_class = InputSerializer
    def get_queryset(self):
        user = self.request.user
        posts = Post.objects.filter(profile__user=user)
        return posts

    @extend_schema(
        responses=serializer_class,
        description="List posts",
        parameters=[
            OpenApiParameter(name='id', type=str, description='ID of the post'),
            OpenApiParameter(name='title', type=str, description='Title of the post'),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        request=Input_serializer_class,
        responses=serializer_class,
        description="Create post",
    )
    def create(self, request, *args, **kwargs):
        serializer = InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        title = serializer.validated_data['title']
        content = serializer.validated_data['content']
        profile = get_profile(user=user)
        post = Post.objects.create(profile=profile, title=title, content=content)
        serializer = PostOutputSerializer(post)
        headers = self.get_success_headers(serializer.data)