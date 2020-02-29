from django.urls import reverse, resolve

from django.test import TestCase

# Create your tests here.

from django.test import TestCase

from polls.views import home


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
