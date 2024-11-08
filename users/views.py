from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def register_view(request):
  if(request.method == "Post"):
    form = UserCreationForm(request.POST)
    if form.is_valid():
      login(request, form.save())
      return redirect("explore/")
    
  else:
    form = UserCreationForm()
  return render(request, 'landingpage.html')

def login_view(request):
  if request.method == "POST":
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      login(request, form.get_user())
      if 'next' in request.POST:
        return redirect(request.POST.get('next'))
      else:
        return redirect("explore/")
  else:
    form = AuthenticationForm()
  return render(request, "landingpage.html")

def logout_view(request):
  if request.method == "POST":
    logout(request)
    return redirect("landingpage.html")