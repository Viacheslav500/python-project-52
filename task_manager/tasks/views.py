from django.views.generic import (DetailView, CreateView,
                                  UpdateView, DeleteView)
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from .mixins import PermitDeleteTaskMixin
from django_filters.views import FilterView
from .filter import TaskFilter
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin


class ListTaskView(LoginRequiredMixin, FilterView):
    template_name = 'tasks/index.html'
    model = Task
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    extra_context = {'button_text': _('Show')}


class CreateTaskView(SuccessMessageMixin, LoginRequiredMixin,
                     CreateView):
    template_name = 'registration/form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task was created')
    extra_context = {'header': _('Create task'),
                     'button_text': _('Create')}

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class UpdateTaskView(SuccessMessageMixin, LoginRequiredMixin,
                     UpdateView):
    template_name = 'registration/form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task was updated')
    extra_context = {'header': _('Update task'),
                     'button_text': _('Update')}


class DeleteTaskView(PermitDeleteTaskMixin, SuccessMessageMixin,
                     LoginRequiredMixin, DeleteView):
    template_name = 'delete_form.html'
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task was deleted')
    extra_context = {'header': _('Delete task'),
                     'button_text': _('Yes, delete')}


class DetailTaskView(LoginRequiredMixin, DetailView):
    template_name = 'tasks/task_detail.html'
    model = Task
