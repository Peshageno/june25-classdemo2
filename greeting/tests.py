"""Tests for greeting views and context data."""

from django.test import TestCase, Client
from django.urls import reverse


class GreetingTests(TestCase):
    """Tests for the greeting index page."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_index_page(self):
        """Test that the index page returns 200 and contains 'Hello'."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello')
        self.assertTemplateUsed(response, 'index.html')


class GreetingFunctionalityTests(TestCase):
    """Tests for greeting context data."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_greeting(self):
        """Test that the greeting context contains 'Hello'."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.context['greeting'], 'Hello')
