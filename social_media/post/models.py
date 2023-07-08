from django.db import models
from social_media.common.models import BaseModel
from social_media.profile.models import Profile
class Post(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField(
                blank = True , 
                default= ""
                
            )
    title = models.CharField(max_length=100 , default="")
    