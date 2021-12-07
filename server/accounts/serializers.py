from rest_framework import fields, serializers
from django.contrib.auth import get_user_model
from community.models import Review
class UserSerializer(serializers.ModelSerializer):
    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ("id",)

    like_reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = get_user_model()
        fields = ("id","username","like_reviews")

