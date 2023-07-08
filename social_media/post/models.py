from django.db import models
from social_media.common.models import BaseModel
from social_media.users.models import Profile
class Post(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(
                blank = True , 
                
            )