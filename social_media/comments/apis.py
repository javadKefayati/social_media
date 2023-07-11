from rest_framework.generics import ListAPIView
from ..post.models import Post
from .models import Comment


class ListCommentsApi(ListAPIView):
    models = Comment
    
    def query_set(self):
        post_id = self.request.query_params.get('post_id')
        