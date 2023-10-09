from rest_framework import status
from rest_framework.response import Response
from social_media.profile.models import Profile
from social_media.profile.selectors import get_profile
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated , IsAdminUser , AllowAny
#from django.shortcuts import get_object_or_404
from social_media.user.services import register  
from social_media.common.permission import IsOwner
from .serializer import UserSerializer


class ProfileApi(
                viewsets.ModelViewSet,
    ):
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'
    ordering = ('created_at')
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action == 'post':
            permission_classes = [IsAuthenticated]
        else :
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return get_profile(user = self.request.user)
        return Profile.objects.none()

    def perform_create(self, serializer):

        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        try:
            # create user with default profile 
            user = register(
                    username = serializer.validated_data.get("username"),
                    email=serializer.validated_data.get("email"),
                    password=serializer.validated_data.get("password"),
                    bio=serializer.validated_data.get("bio"),
                    is_admin=False,
                    )
            
        except Exception as ex:
            return Response(
                    f"Database Error {ex}",
                    status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(self.serializer_class(user, context={"request":self.request}).data)

    

