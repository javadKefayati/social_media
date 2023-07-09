from django.urls import path
# from .apis import PostApi
from .apis import PostList
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'cutarea', PostList,    basename='cutareadel')

urlpatterns = [
    # url(r'^apidsf/', include(router.urls)),
    # path('', PostList.as_view({'get': 'list'}),name="post api1"),
]
urlpatterns += router.urls