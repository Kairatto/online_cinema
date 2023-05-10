from django.urls import path, include
from rest_framework import routers

from .views import CommentViewSet, CategoryViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:pk>/video/', MovieViewSet.as_view({'get': 'get_video'}), name='movie-video'),
    path('movies/<int:pk>/image/', MovieViewSet.as_view({'get': 'get_image'}), name='movie-image'),
]

