from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Genre, Movie, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie','user')

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    # class CommentSerializer(serializers.ModelSerializer):
    #     model = Comment
    #     fields = "__all__"
    comment_set = CommentSerializer(many=True,read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('comment_set', 'genre')

class MovieCommentSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True,read_only=True)
    
    class Meta:
        model = Movie
        fields = ('comment_set',)
        read_only_fields = ('comment_set',)

