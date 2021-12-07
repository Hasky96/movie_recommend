from django.urls import path
from . import views

urlpatterns = [
    # 전체리뷰
    path('reviews/', views.all_reviews),
    # 리뷰생성
    path('<int:movie_pk>/new_review/', views.reviews_create),
    # 리뷰의 detail
    path('review/<int:review_pk>/', views.reviews_detail),
    # 리뷰의 like
    path('review/<int:review_pk>/like/', views.like_review),
    # 리뷰의 comment
    path('review/<int:review_pk>/comment/', views.comment_create),
    # 특정영화 ID의 리뷰만 주세요
    path('movie/<int:movie_id>/reviews/', views.review_by_movieID),
    # 리뷰의 코멘트 다주세요
    path('review/<int:review_pk>/comments/', views.comments),
    # 리뷰 수정, 삭제
    path('review/<int:review_pk>/updel/', views.review_detail_or__update_or_delete),
    # 리뷰 수정, 삭제
    path('comments/<int:comment_pk>/del/', views.comments_delete),

]
