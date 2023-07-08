from .models import Post
def get_profile(request, post_id)-> Post:
    user = request.user
    
    profile = Post.objects.get(user= user)
    post = Post.objects.get(
                            profile = profile,
                            id      = Post_id, 
                            )
    return post