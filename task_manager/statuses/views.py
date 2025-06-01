from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    ListView
)
from .models import Status
from .forms import StatusForm
from django.urls import reverse_lazy
from task_manager.mixins import DeleteProtectionMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin


class ListStatusView(LoginRequiredMixin, ListView):
    template_name = 'statuses/index.html'
    model = Status
    context_object_name = 'statuses'


class CreateStatusView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'registration/form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status was created')
    extra_context = {'header': _('Create status'), 'button_text': _('Create')}


class UpdateStatusView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'registration/form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status was updated')
    extra_context = {'header': _('Update status'), 'button_text': _('Update')}


class DeleteStatusView(LoginRequiredMixin, DeleteProtectionMixin,
                       SuccessMessageMixin, DeleteView):
    template_name = 'delete_form.html'
    model = Status
    success_url = reverse_lazy('statuses')
    protected_url = reverse_lazy('statuses')
    success_message = _('Status was deleted')
    protected_message = _('Impossible to delete status because it is in use')
    extra_context = {'header': _('Delete status'),
                     'button_text': _('Yes, delete')}
