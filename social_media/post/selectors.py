from .models import Post
def get_profile(requst, post_id)-> Post:
    post = Post.objects.get(user=user, id= Post_id)
    return post