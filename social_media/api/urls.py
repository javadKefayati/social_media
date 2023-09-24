from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path('auth/', include(('social_media.authentication.urls', 'auth'))),
    path('profile/', include(('social_media.profile.urls', 'profile'))),
    path('post/', include(('social_media.post.urls', 'post')),name="post apis"),
    path('test/', include(('social_media.test_code.urls', 'post')),name="test apis"),
]
