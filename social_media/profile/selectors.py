from .models import Profile

def get_profile(user:BaseUser) -> Profile:
    return Profile.objects.get(user=user)
