from django.db import models
from TaskCategory.models import TaskCategory
# Create your models here.

class TaskModel(models.Model):
    id = models.AutoField(primary_key=True)
    TaskTitle = models.CharField(max_length=50)
    TaskDescription = models.TextField()
    isCompleted = models.BooleanField(default=False)
    TaskAssignDate = models.DateTimeField(auto_now_add=True)
    Category = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.TaskTitle
