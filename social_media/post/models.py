from django.db import models
from social_media.common.models import BaseModel
class Post(BaseModel):
    text = models.TextField(
                blank = True , 
                
            )