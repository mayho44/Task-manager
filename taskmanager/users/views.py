from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from tasks.models import *

# Create your views here.
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.POST.get('next') or request.GET.get('next')
            return redirect(next_url or 'all_tasks')
    else:
        form = AuthenticationForm()

    return render(request, "users/log_in.html", {'form': form})

def log_out(request):
  if request.method == 'POST':
    logout(request)
    return redirect('home')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("all_tasks")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {'form': form})

