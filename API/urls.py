from django.urls import include, path
from rest_framework import routers

# from .views import (CategoryViewSet, CommentViewSet,
#                     GenreViewSet, ReviewViewSet, TitleViewSet)

v1_router = routers.DefaultRouter()
# v1_router.register('titles', TitleViewSet, basename='title')
# v1_router.register('categories', CategoryViewSet, basename='categories')
# v1_router.register('genres', GenreViewSet, basename='genres')
# v1_router.register(r'titles/(?P<title_id>\d+)/reviews',
#                    ReviewViewSet, basename='reviews')
# v1_router.register(r'titles/(?P<title_id>\d+)'
#                    r'/reviews/(?P<review_id>\d+)/comments',
#                    CommentViewSet, basename='comments')


urlpatterns = [
    path('', include(v1_router.urls)),
    # Эндпоинты для управления пользователями в Django:
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path("auth/", include("djoser.urls.jwt")),
]
