from django.urls import path
from . import views

urlpatterns = [
    # 전체영화
    path('list/', views.movies),
    # pagination
    path('list/<int:page_num>/', views.page),
    # pagination total page
    path('list/totalpages/', views.totalpage),
    # 단일영화
    path('<int:movie_pk>/info/', views.movie_detail),
    # 영화 한줄평
    path('<int:movie_pk>/comment_create/', views.comment_create),
    # 한줄평 전부
    path('<int:movie_pk>/comments/', views.comments),
    # 한줄평 좋아요
    path('<int:movie_pk>/<int:comment_pk>/like/', views.like_comment),
    # 영화리스트 제목
    path('search/<int:page_num>/', views.search),
    # 메인페이지 슬롯 용 영화 찾기
    path('slot/', views.slot_search),
    # 장르
    path('<int:movie_pk>/genres/', views.genre),
    # 코멘트 삭제
    path('comments/<int:comment_pk>/del/', views.comment_del)

]
