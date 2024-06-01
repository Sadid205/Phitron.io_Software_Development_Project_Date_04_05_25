from django import forms
from .models import TaskModel


class TaskModelForm(forms.ModelForm):
   class Meta:
        model = TaskModel
        fields = "__all__"
        labels = {
            'TaskTitle': 'Task Title',
            'TaskDescription':'Task Description',
            'isCompleted':'Completed'
        }