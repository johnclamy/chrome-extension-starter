from django.contrib import admin
from . models import Movie


class MovieAdmin(admin.ModelAdmin):
  ordering = ['title']
  search_fields = ['title']


admin.site.register(Movie, MovieAdmin)
