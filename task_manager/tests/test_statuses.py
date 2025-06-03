from django.test import TestCase
from task_manager.statuses.models import Status
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class StatusTestCase(TestCase):
    fixtures = ['tests/fixtures/users.json', 'tests/fixtures/statuses.json']

    def setUp(self):
        self.new_status = {
            'name': 'Not in progress'
        }

    def test_status_create(self):
        self.client.force_login(get_user_model().objects.get(id=1))
        response = self.client.get(reverse('create_status'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('create_status'),
                                    data=self.new_status,
                                    follow=True
                                    )
        self.assertContains(response, _('Status was created'))
        count_statuses = Status.objects.count()
        self.assertEqual(count_statuses, 4)

    def test_read(self):
        self.client.force_login(get_user_model().objects.get(id=1))
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'in progress')

    def test_update(self):
        self.client.force_login(get_user_model().objects.get(id=1))
        response = self.client.post(reverse('update_status', kwargs={'pk': 1}),
                                    data=self.new_status, follow=True)
        self.assertRedirects(response, reverse('statuses'))
        self.assertEqual(Status.objects.get(pk=1).name, 'Not in progress')
        self.assertContains(response, _('Status was updated'))

    def test_delete(self):
        self.client.force_login(get_user_model().objects.get(id=1))
        response = self.client.post(reverse('delete_status',
                                    kwargs={'pk': 2}),
                                    follow=True
                                    )
        self.assertRedirects(response, reverse('statuses'))
        self.assertContains(response, _('Status was deleted'))
