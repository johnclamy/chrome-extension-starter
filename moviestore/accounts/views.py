from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from . forms import CustomUserCreationForm, CustomErrorList


def signup(request):
  template_data = {}
  template_data['title'] = 'Sign up'

  if request.method == 'GET':
    template_data['form'] = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'template_data': template_data})
  
  elif request.method == 'POST':
    form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)

    if form.is_valid():
      form.save()
      return redirect('home.index')
    else:
      template_data['form'] = form
      return render(request, 'accounts/signup.html', {'template_data': template_data})


def signin(request):
  template_data = {}
  template_data['title'] = 'Signin'

  if request.method == 'GET':
    return render(request, 'accounts/signin.html', {'template_data': template_data})
  elif request.method == 'POST':
    user = authenticate(
      request,
      username = request.POST['username'],
      password = request.POST['password']
    )

    if user is None:
      template_data['error'] = 'Username or password is incorrect.'
      return render(request, 'accounts/signin.html', {'template_data': template_data})
    else:
      auth_login(request, user)
      return redirect('home.index')
    

