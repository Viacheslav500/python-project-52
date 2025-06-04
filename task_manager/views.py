from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, _("You have successfully logged out."))
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'registration/form.html'
    next_page = reverse_lazy('home')
    success_message = _('User is logged in')
    extra_context = {'header': _('Log In'), 'button_text': _('login')}
