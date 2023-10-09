from rest_framework import serializers
from social_media.profile.models import Profile
from social_media.user.serializer import UserSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class OutPutSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField("get_token")
    user = UserSerializer

    class Meta:
        model = Profile 
        fields = ("user","bio", "posts_count", "follower_count", "following_count","token")
        extra_kwargs = {
            'posts_count': {'read_only': True},
            'follower_count': {'read_only': True},
            'following_count': {'read_only': True},
        }        

    def get_token(self, user):
        data = dict()
        token_class = RefreshToken

        refresh = token_class.for_user(user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data
    


