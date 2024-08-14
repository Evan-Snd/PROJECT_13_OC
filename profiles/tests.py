from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from unittest.mock import patch

class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profiles_index_view(self):
        response = self.client.get(reverse('profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertTemplateUsed(response, 'profiles_index.html')

    def test_profile_view(self):
        response = self.client.get(reverse('profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Paris')
        self.assertTemplateUsed(response, 'profile.html')

    def test_profile_view_not_found(self):
        response = self.client.get(reverse('profile', args=['nonexistentuser']))
        result = response.status_code
        self.assertEqual(result, 404)

    @patch('profiles.views.Profile.objects.get')
    def test_profile_view_raises_exception(self, mock_get):
        mock_get.side_effect = Exception('Test Exception')
        response = self.client.get(reverse('profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 500)
