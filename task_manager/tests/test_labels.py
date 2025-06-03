from django.test import TestCase
from task_manager.labels.models import Label
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class StatusTestCase(TestCase):
    fixtures = ['tests/fixtures/users.json', 'tests/fixtures/labels.json']

    def setUp(self):
        self.new_label = {
            'name': 'asdasd'
        }

    def test_labels_create(self):
        self.client.force_login(get_user_model().objects.get(id=1))
        response = self.client.get(reverse('create_label'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('create_label'),
                                    data=self.new_label,
                                    follow=True
                                    )
        self.assertContains(response, _('Label was created'))
        count_statuses = Label.objects.count()
        self.assertEqual(count_statuses, 3)

    def test_read(self):
        self.client.force_login(get_user_model().objects.get(id=1))
        response = self.client.get(reverse('labels'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'mine')

    def test_update(self):
        self.client.force_login(get_user_model().objects.get(id=1))
        response = self.client.post(reverse('update_label', kwargs={'pk': 1}),
                                    data=self.new_label, follow=True)
        self.assertRedirects(response, reverse('labels'))
        self.assertEqual(Label.objects.get(pk=1).name, 'asdasd')
        self.assertContains(response, _('Label was updated'))

    def test_delete(self):
        self.client.force_login(get_user_model().objects.get(id=1))
        response = self.client.post(reverse('delete_label',
                                    kwargs={'pk': 2}),
                                    follow=True
                                    )
        self.assertRedirects(response, reverse('labels'))
        self.assertContains(response, _('Label was deleted'))
