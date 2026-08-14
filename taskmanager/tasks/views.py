from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from tasks.models import *
from django.views.decorators.cache import never_cache, cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request) :
  return render(request, 'tasks/home.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def all_tasks(request):
  if not request.user.is_authenticated:return redirect('home')
  
  tasks = Task.objects.filter(user=request.user)
  Categories = Category.objects.all()
  
  return render(request, 'tasks/task.html', {'tasks':tasks, 'categories':Categories})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="log_in")
def delete_task(request, task_id):
  if not request.user.is_authenticated:return redirect('home')
  task = get_object_or_404(Task, id = task_id, user= request.user)
  task.delete()
  return redirect('all_tasks')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="log_in")
def check_task (request, task_id):
  if not request.user.is_authenticated:return redirect('home')
  Task.objects.filter(id = task_id, user= request.user).update(completion_status = True)
  return redirect('all_tasks')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="log_in")
def search(request):
  if not request.user.is_authenticated:return redirect('home')
  tasks = Task.objects.filter(user=request.user)
  title = request.GET.get('title')
  category_id = request.GET.get('category')

  if title:
    tasks = tasks.filter(title__icontains = title)
  if category_id:
    tasks = tasks.filter(category_id = category_id)
  Categories = Category.objects.all()

  return render(request, 'tasks/task.html', {'tasks':tasks, 'categories': Categories})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="log_in")
def view_task(request, task_id):
  if not request.user.is_authenticated:return redirect('home')
  task = get_object_or_404(Task, id = task_id, user=request.user)
  return render(request, 'tasks/view_task.html',{'task':task})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="log_in")
def add_task(request):
    if not request.user.is_authenticated:return redirect('home')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        completion_status = request.POST.get('completion_status') == 'on'
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        selected_tag_ids = request.POST.getlist('tags')

        category = get_object_or_404(Category, id=category_id) if category_id else None

        task = Task.objects.create(
            title=title,
            description=description,
            completion_status=completion_status,
            due_date=due_date or None,
            priority=priority,
            category=category,
            user=request.user,
        )
        task.tags.set(selected_tag_ids)  

        return redirect('all_tasks')

    return render(request, 'tasks/add_task.html', {'categories': categories, 'tags': tags})
