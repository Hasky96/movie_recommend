from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.signup),
    path('<int:user_num>/', views.userinfo),
    path('api-token-auth/', obtain_jwt_token),
    path('liked-reviews/', views.liked_reviews)
]
