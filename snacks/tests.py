from django.test import TestCase, Client
from django.urls import reverse

class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_home_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_view_contains_text(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'Welcome to the Home Page')

class AboutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('about')

    def test_about_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_about_view_contains_text(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'This is the About Page')

