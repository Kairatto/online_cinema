from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Comment, Movie, Category


class MovieSerializer(serializers.ModelSerializer):
    video_url = serializers.HyperlinkedIdentityField(view_name='movie-video', format='html')
    image_url = serializers.HyperlinkedIdentityField(view_name='movie-image', format='html')

    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
