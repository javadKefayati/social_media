from django.urls import path
from .apis import ProfileApi


urlpatterns = [
    path('profile/', ProfileApi.as_view(),name="register"),
]
