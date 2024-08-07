from django.test import TestCase
from django.urls import reverse

class IndexViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_custom_404_view(self):
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_trigger_error_view(self):
        response = self.client.get('/trigger-error/')
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, '500.html')
