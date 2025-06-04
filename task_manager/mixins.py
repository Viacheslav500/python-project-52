from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.views.generic.edit import DeletionMixin
from django.utils.translation import gettext as _


class PermitModifyUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().id == self.request.user.id

    def handle_no_permission(self):
        message = _('You do not have permissions to modify user')
        messages.error(self.request, message)
        return redirect(reverse_lazy('users'))


class DeleteProtectionMixin(DeletionMixin):
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
