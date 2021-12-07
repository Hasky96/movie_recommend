from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from community.models import Review
from movies.models import Movie
from .serializers import ReviewListSerializer, ReviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET'])
@permission_classes([AllowAny])
def all_reviews(request):
    reviews = Review.objects.order_by("-pk")
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([AllowAny])
def reviews_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)# user= request.user
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def reviews_detail(request,movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_200_OK)
