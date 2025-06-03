from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class PermitDeleteTaskMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().creator != request.user:
            message = _('A task can only be deleted by its user')
            messages.error(request, message)
            return redirect("tasks")
        return super().dispatch(request, *args, **kwargs)
