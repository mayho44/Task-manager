from django.urls import path
from . import views
urlpatterns = [
  path('all_tasks/', views.all_tasks, name="all_tasks"),
  path('', views.index, name = 'home'),
  path('check/<int:task_id>',views.check_task, name ='check_task'),
  path('search/', views.search,name = 'search'),
  path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
  path('task_view/<int:task_id>/', views.view_task, name='view_task'),
  path('add_task/', views.add_task, name='add_task'),
]