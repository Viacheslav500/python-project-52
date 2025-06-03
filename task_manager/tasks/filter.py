import django_filters
from .models import Task
from task_manager.labels.models import Label
from django import forms
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):
    own_tasks = django_filters.BooleanFilter(
        method='show_own_task',
        widget=forms.CheckboxInput,
        label=_('Show own tasks'),
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label')
    )

    def show_own_task(self, queryset, arg, value):
        user = self.request.user if self.request else None
        return queryset.filter(creator=user) if value else queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
