from django.db import transaction 
from social_media.profile.models import Profile
from django.contrib.auth import get_user_model


def create_profile(*, user:get_user_model(), bio:str | None) -> Profile:
    return Profile.objects.create(user=user, bio=bio)

def create_user(*,username:str, email:str, password:str, is_admin:bool) -> get_user_model():
    return get_user_model().objects.create_user(username=username, email=email, password=password, is_admin=is_admin)


@transaction.atomic
def register(*,username:str, bio:str|None, email:str, password:str, is_admin:bool) -> get_user_model():

    user = create_user(username=username ,email=email, password=password,is_admin=is_admin)
    create_profile(user=user, bio=bio)

    return user
