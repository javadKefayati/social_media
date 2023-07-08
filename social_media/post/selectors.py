from .models import Post
from ..profile.models import Profile
from ..profile.selectors import get_profile
def get_post(user, post_id=None)-> Post:
    profile = get_profile(user)
    #if you want all post
    if post_id is None:
        posts = Post.objects.all()
        return posts
    # If you want specified post
    else :
        
        try :
            post = Post.objects.get(
                                    profile = profile,
                                    id      = int(post_id)
                                    )

        except Exception as ex:
            post = Post()

        return post