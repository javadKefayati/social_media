from django.urls import path
# from .apis import PostApi
from .apis import ListCommentsApi
from rest_framework import routers
router = routers.DefaultRouter()
# router.register(r'', PostList,    basename='cutareadel')

urlpatterns = [
    # url(r'^apidsf/', include(router.urls)),
    path('', ListCommentsApi.as_view(),name="post api1"),
]
# urlpatterns += router.urls