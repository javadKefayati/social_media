from rest_framework import serializers
from social_media.post.models import Post
from social_media.api.mixins import ApiAuthMixin
from .selectors import get_post
import django_filters
from drf_spectacular.utils import extend_schema, OpenApiParameter,extend_schema_field
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from social_media.profile.selectors import get_profile
from rest_framework import viewsets
from social_media.profile.models import  Profile

class PostFilterSet(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['id', 'title']





class PostOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        
        fields = ("id", "content", "title", "created_at", "updated_at")
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }



class PostList(
            ApiAuthMixin,
            viewsets.ModelViewSet,
            ):
    serializer_class = PostOutputSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilterSet
    ordering_fields = '__all__'
    ordering = ('created_at')


    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            # TODO ordered with created_at list posts
            return Post.objects.filter(profile__user=user)
        return Post.objects.none()


    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(profile=profile)

    



