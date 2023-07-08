from .models import Post
def get_post(user, post_id)-> Post:
    profile = Post.objects.get(user= user)
    post = Post.objects.get(
                            profile = profile,
                            id      = Post_id, 
                            )
    return post