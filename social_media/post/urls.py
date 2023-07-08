from django.urls import path
from .apis import PostApi


urlpatterns = [
    path('get/<int:post_id>', PostApi.as_view(),name="post api"),
]
