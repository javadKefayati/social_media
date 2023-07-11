from django.urls import path, include

from .apis import GetTestApi

urlpatterns = [
    path("list/", GetTestApi.as_view(), name="schema"),

]
