from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class SmokeTest(TestCase):

    def test_root_url__resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
