from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    TASK_STATUS = (
        ('on_hold', 'On Hold'),
        ('complete', 'Complete'),
        ('in_progress', 'In Progress'),
        ('to_do', 'To Do'),
    )
    task = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='ToDoList')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='to do')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.task
