from django.urls import path
from .apis import PostApi


urlpatterns = [
    path('post/<int:post_id>', PostApi.as_view(),name="post api"),
]
