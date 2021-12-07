from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from movies.serializers import CommentSerializer, MovieSerializer
from rest_framework import status
from .models import Movie
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def movies(request):
    movies_list = Movie.objects.all()
    serializer = MovieSerializer(movies_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def movie_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie) # user= request.user
        return Response(serializer.data, status=status.HTTP_201_CREATED)