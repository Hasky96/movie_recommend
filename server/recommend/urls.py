from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_recommend),
    path('movie/', views.show_recommend_movie),
    path('title/', views.title_recommend),
    path('catch/', views.catch_data),
    path('<int:movie_pk>/detail/', views.detail_recommend),
]
