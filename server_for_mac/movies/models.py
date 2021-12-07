from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, null=False)
    # release_date = models.DateField()
    release_date = models.CharField(max_length=40)
    vote_count = models.PositiveIntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments', blank=True)
    rank = models.PositiveIntegerField()

    def __str__(self):
        return f"comment : {self.content}"

class Genre(models.Model):
    name = models.CharField(max_length=50)
    movie = models.ManyToManyField(Movie, related_name='genre')

    def __str__(self):
        return self.name