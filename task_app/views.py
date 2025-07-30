from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from task_app.forms import TaskForm
from .models import Task # Припустимо, у вас є модель Post

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)  