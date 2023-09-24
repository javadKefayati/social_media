from django.urls import path
from .apis import ProfileApi
from social_media.users import RegisterProfileApi


urlpatterns = [
    path('get/', ProfileApi.as_view(),name="get profile "),
    path('register/', RegisterProfileApi.as_view(),name="register"),

]
