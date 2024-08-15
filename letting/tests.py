from django.test import TestCase
from django.urls import reverse
from .models import Letting, Address
# from unittest.mock import patch


class LettingViewTests(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="Anytown",
            state="CA",
            zip_code=90210,
            country_iso_code="USA"
        )
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_lettings_index_view(self):
        response = self.client.get(reverse('lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Letting')
        self.assertTemplateUsed(response, 'lettings_index.html')

    def test_letting_view(self):
        response = self.client.get(reverse('letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Letting')
        self.assertTemplateUsed(response, 'letting.html')

    def test_letting_view_not_found(self):
        response = self.client.get(reverse('letting', args=[999]))
        self.assertEqual(response.status_code, 404)

    '''@patch('letting.views.Letting.objects.get')
    def test_letting_view_raises_exception(self, mock_get):
        mock_get.side_effect = Exception('Test Exception')
        response = self.client.get(reverse('letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 500)
'''
