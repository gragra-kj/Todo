from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class TodoModel(models.Model):
    STATUS_PENDING = 'PENDING'
    STATUS_IN_PROGRESS = 'IN_PROGRESS'
    STATUS_COMPLETED = 'COMPLETED'
    
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_COMPLETED, 'Completed'),
    ]
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="todo")
    title=models.CharField(max_length=200)
    description=models.TextField()
    due_date=models.DateTimeField(null=True,blank=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default=STATUS_PENDING)
    created_at=models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    
    def __str__(self):
        return self.title