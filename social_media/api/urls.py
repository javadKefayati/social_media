from django.urls import path, include

urlpatterns = [
    # path('blog/', include(('social_media.blog.urls', 'blog')))
    path('auth/', include(('social_media.authentication.urls', 'auth'))),
    path('user/', include(('social_media.users.urls', 'authentication'))),
]
