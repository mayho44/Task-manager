from django.db import models
from django.contrib.auth.models import User



# Create your models here. 

class Category(models.Model):
  category_name = models.CharField(max_length=50)
  def __str__(self):
    return self.category_name.title()

class Tag (models.Model):
  tag_name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.tag_name.title()

class Task(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True, default='')
  completion_status = models.BooleanField(default=False)
  due_date = models.DateField(blank=True, null=True)
  priority_choices = [
    ( 'high','High'),
    ( 'low','Low')
  ]
  priority = models.CharField(max_length=5, choices=priority_choices)
  tags = models.ManyToManyField(Tag, blank=True, related_name='tasks')

  category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    null = True,
    blank=True,
  )
  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE, 
  )

  def __str__(self):
    return self.title


