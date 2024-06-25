from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.

class BlogTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response= "welcome to the Home Page")

class BlogTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Test Post', body='This is a test post.')
      
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Home Page")