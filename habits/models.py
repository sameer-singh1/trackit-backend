from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    frequency = models.CharField(max_length=10,choices=[
        ('daily','Daily'),
        ('weekly','Weekly'),
        ('monthly','Monthly') 
    ])
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.name}({self.user.username})'
