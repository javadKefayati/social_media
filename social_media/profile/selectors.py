from .models import Profile

def get_profile(user) -> Profile:
    print(user)
    return Profile.objects.get(user=user)
