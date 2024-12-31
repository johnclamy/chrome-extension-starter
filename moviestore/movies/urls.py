from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='movie.index'),
  path('<int:id>/', views.show, name='movies.show'),
]
