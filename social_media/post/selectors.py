from .models import Post
from ..profile.models import Profile
from ..profile.selectors import get_profile
def get_post(user, post_id)-> Post:

    profile = get_profile(user)
    print(profile.id)
    
    post = Post.objects.get(
                            profile = profile,
                            id      = int(post_id)
                            )
    
    print(post.text)
    return post