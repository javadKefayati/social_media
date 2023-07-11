from django.db import models
from social_media.common.models import BaseModel
from ..users.models import BaseUser
from ..post.models import Post

class Comment(BaseModel):
    author = models.ForeignKey(BaseUser, on_delete=models.SET_NULL , null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    
    