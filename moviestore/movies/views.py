from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Movie,Review


def index(request):
  template_data = {}
  template_data['title'] = 'Movies'
  search_term = request.GET.get('search')

  if search_term:
    movies = Movie.objects.filter(title__icontains=search_term)
  else:
    movies = Movie.objects.all()

  template_data['movies'] = movies
  return render(request, 'movies/index.html', {'template_data': template_data})


def show(request, id):
  movie = Movie.objects.get(id=id)
  template_data = {}
  template_data['title'] = movie.title
  template_data['movie'] = movie

  return render(request, 'movies/show.html', {'template_data': template_data})


@login_required
def create_review(request, id):
  if request.method == 'POST' and request.POST['comment'] != '':
    movie = Movie.objects.get(id=id)
    review = Review()

    review.comment = request.POST['comment']
    review.movie = movie
    review.user = request.user
    review.save()

    return redirect('movies.show', id=id)
  else:
    return redirect('movies.show', id=id)