from django.urls import path
from . import views

urlpatterns = [
    # 전체영화
    path('list/', views.movies),
    # 단일영화
    path('<int:movie_pk>/info/', views.movie_detail),
    # 영화 한줄평
    path('<int:movie_pk>/comment/', views.movie_comment),
]
