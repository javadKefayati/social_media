from django.urls import path
from .apis import ProfileApi


urlpatterns = [
    path('get/', ProfileApi.as_view(),name="get profile "),
]
