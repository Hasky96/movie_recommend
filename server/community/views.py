from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from community.models import Review, Comment
from movies.models import Movie
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET'])
@permission_classes([AllowAny])
def all_reviews(request):
    reviews = Review.objects.order_by("-pk")
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def reviews_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user= request.user)# 
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def reviews_detail(request,review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user= request.user)# 
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def like_review(request,review_pk):
    me = request.user
    review = get_object_or_404(Review,pk=review_pk)
    print(review.like_users)
    if review.like_users.filter(pk=me.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    context = {
         'review' : review.like_users.count()
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([AllowAny])
def review_by_movieID(request, movie_id):
    reviews =Review.objects.filter(movie_id=movie_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([AllowAny])
def comments(request, review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    comments =review.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(["DELETE"])
def comments_delete(request, comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if comment.user == request.user:
        if request.method == 'DELETE':
            print('delete 넘었음')
            comment.delete()
            data =  {
                'message' : f'리뷰 {comment_pk} 가 사라졌습니다',
            }
            return Response(data,status = status.HTTP_204_NO_CONTENT)
    return Response(status = status.HTTP_403_FORBIDDEN)

@api_view(['GET','PUT','DELETE'])
def review_detail_or__update_or_delete(request,review_pk):
    print('삭제 페이지 진입 합')
    review = get_object_or_404(Review,pk=review_pk)
    print('404 넘었음')
    if review.user == request.user:
        print('user 넘었음')
        if request.method == 'PUT':
            print('update 넘었음')
            serializer = ReviewSerializer(review, data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        elif request.method == 'DELETE':
            print('delete 넘었음')
            review.delete()
            data =  {
                'message' : f'리뷰 {review_pk} 가 사라졌습니다',
            }
            return Response(data,status = status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
