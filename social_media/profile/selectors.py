from .models import Profile

def get_profile(user) -> Profile:
    return Profile.objects.get(user=user)
