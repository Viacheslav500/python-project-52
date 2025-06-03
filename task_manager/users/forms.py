from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'password1', 'password2')


PASS_WIDGET = forms.PasswordInput(attrs={'class': 'form-control'})


class UpdateUserForm(UserChangeForm):
    password = None
    password1 = forms.CharField(
        label=_('Password'),
        widget=PASS_WIDGET,
        help_text=_('Your password should be longer 3 characters'))
    password2 = forms.CharField(
        label=_('Password Confirmation'),
        widget=PASS_WIDGET,
        help_text=_('Enter your password again'))

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('pssword1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2
