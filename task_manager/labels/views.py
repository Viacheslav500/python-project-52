from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    ListView
)
from django.urls import reverse_lazy
from .models import Label
from .forms import LabelForm
from task_manager.mixins import DeleteProtectionMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin


class LabelsListView(LoginRequiredMixin, ListView):
    template_name = 'labels/index.html'
    model = Label
    context_object_name = 'labels'


class LabelCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'registration/form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label was created')
    extra_context = {'header': _('Create Label'), 'button_text': _('Create')}


class LabelUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'registration/form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label was updated')
    extra_context = {'header': _('Update Label'), 'button_text': _('Update')}


class LabelDeleteView(DeleteProtectionMixin, LoginRequiredMixin,
                      SuccessMessageMixin, DeleteView):
    template_name = 'delete_form.html'
    model = Label
    success_url = reverse_lazy('labels')
    protected_url = reverse_lazy('labels')
    success_message = _('Label was deleted')
    protected_message = _('Impossible to delete because it is in use')
    extra_context = {'header': _('Delete Label'),
                     'button_text': _('Yes, delete')}
