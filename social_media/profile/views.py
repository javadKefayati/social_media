
from django.urls import path
from .apis import Post


urlpatterns = [
    path('profile/<int:post_id>', ProfileApi.as_view(),name="register"),
]
