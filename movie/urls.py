from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import CommentViewSet, CategoryViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'movies', MovieViewSet, basename='movie')

schema_view = get_schema_view(
    openapi.Info(
        title="Post API",
        default_version='v1',
        description="API for movies",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@movies.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('movies/<int:pk>/video/', MovieViewSet.as_view({'get': 'get_video'}), name='movie-video'),
    path('movies/<int:pk>/image/', MovieViewSet.as_view({'get': 'get_image'}), name='movie-image'),
]

