from django.urls import path
from .apis import detail_post


urlpatterns = [
    path('get/<int:post_id>', detail_post.as_view(),name="post api"),
]
