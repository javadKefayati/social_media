from django.urls import path
from .apis import ProfileApi
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', ProfileApi,    basename='profile route')
urlpatterns = []
urlpatterns += router.urls
