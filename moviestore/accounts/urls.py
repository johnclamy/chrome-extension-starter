from django.urls import path
from . import views


urlpatterns = [
  path('signup', views.signup, name='accounts.signup'),
  path('signin', views.signin, name='accounts.signin'),
  path('sign-out/', views.sign_out, name='accounts.sign-out'),
]
