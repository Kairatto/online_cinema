from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import IsAuthorOrAllowAny, MoviePermission, CategoryPermission
from .serializers import CommentSerializer, MovieSerializer, CategorySerializer
from .models import Comment, Movie, Category


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [MoviePermission, ]

    @action(detail=True, methods=['get'])
    def get_video(self, request, pk=None):
        movie = self.get_object()
        video_url = movie.video.url
        return Response({'url': video_url})

    @action(detail=True, methods=['get'])
    def get_image(self, request, pk=None):
        movie = self.get_object()
        image_url = movie.image.url
        return Response({'image_url': image_url})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthorOrAllowAny, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermission, ]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
