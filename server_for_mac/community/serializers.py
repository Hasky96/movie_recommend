from rest_framework import serializers
from movies.serializers import MovieSerializer
from .models import Review
from movies.models import Movie


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = "__all__"
        movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ('movie',)