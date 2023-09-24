from django.urls import path
from .apis import ProfileApi
from social_media.users import RegisterApi


urlpatterns = [
    path('get/', ProfileApi.as_view(),name="get profile "),
    path('register/', RegisterApi.as_view(),name="register"),

]
