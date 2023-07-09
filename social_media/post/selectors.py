from .models import Post
from ..profile.models import Profile
from ..profile.selectors import get_profile
def get_post(*, user)-> Post:
    profile = get_profile(user)
    #if you want all post
    posts = Post.objects.filter(profile = profile)
    return posts
