from django.contrib import admin
from .models import Tag, Task, Category

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Tag)