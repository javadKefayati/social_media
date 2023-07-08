from django.urls import path, include

urlpatterns = [
    # path('blog/', include(('social_media.blog.urls', 'blog')))
    path('auth/', include(('social_media.authentication.urls', 'auth'))),
    path('user/', include(('social_media.users.urls', 'register'))),
    path('profile/', include(('social_media.profile.urls', 'profile'))),
    path('post/', include(('social_media.post.urls', 'post'))),
]
