from django.db import models


class Movie(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  price = models.IntegerField()
  descr = models.TextField()
  image = models.ImageField(upload_to='movie_imgs/')

  def __str__(self) -> str:
    return str(self.id) + ' - ' + self.title
