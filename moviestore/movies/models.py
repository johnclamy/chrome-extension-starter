from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  price = models.IntegerField()
  descr = models.TextField()
  image = models.ImageField(upload_to='movie_imgs/')

  def __str__(self):
    return str(self.id) + ' - ' + self.title


class Review(models.Model):
  id = models.AutoField(primary_key=True)
  comment = models.CharField(max_length=255)
  date = models.DateTimeField(auto_now_add=True)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.id) + ' - ' + self.movie.title
