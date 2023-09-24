from django.urls import path
from .apis import RegisterProfileApi


urlpatterns = [
    path('register/', RegisterProfileApi.as_view(),name="register"),
]
