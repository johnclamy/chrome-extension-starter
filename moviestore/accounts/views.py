from django.shortcuts import render, redirect
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
