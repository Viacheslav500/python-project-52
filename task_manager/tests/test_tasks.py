from django.test import TestCase
from task_manager.tasks.models import Task
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class StatusTestCase(TestCase):
    fixtures = ['tests/fixtures/users.json', 'tests/fixtures/labels.json',
                'tests/fixtures/statuses.json', 'tests/fixtures/task.json'
                ]

    def setUp(self):
        self.new_task = {
            'name': 'asdasd',
            'description': 'asdsasd',
            'status': 1
        }

    def test_task_create(self):
        self.client.force_login(get_user_model().objects.get(id=1))
        response = self.client.get(reverse('create_task'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('create_task'),
                                    data=self.new_task,
                                    follow=True
                                    )
        self.assertContains(response, _('Task was created'))
        count_statuses = Task.objects.count()
        self.assertEqual(count_statuses, 3)

    def test_read(self):
        self.client.force_login(get_user_model().objects.get(id=1))
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task 1')

    def test_update(self):
        self.client.force_login(get_user_model().objects.get(id=1))
        response = self.client.post(reverse('update_task', kwargs={'pk': 1}),
                                    data=self.new_task, follow=True)
        self.assertRedirects(response, reverse('tasks'))
        self.assertEqual(Task.objects.get(pk=1).name, 'asdasd')
        self.assertContains(response, _('Task was updated'))

    def test_delete(self):
        self.client.force_login(get_user_model().objects.get(id=2))
        response = self.client.post(reverse('delete_task',
                                    kwargs={'pk': 2}),
                                    follow=True
                                    )
        self.assertRedirects(response, reverse('tasks'))
        self.assertContains(response, _('Task was deleted'))
