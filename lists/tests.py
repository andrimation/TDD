from django.urls import resolve
from lists.views import home_page
from django.test import TestCase
# django.test -> to rozszeżona wersja unittest dla django !

# Create your tests here.

# class SmokeTest(TestCase):
#
#     def test_bad(self):
#         self.assertEqual(1+1,3)

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # resolve służy dopasowaniu adresu url do konkretnej funkcji widoku. - zwraca
        # funkcję która ma zostać wykonana po otrzymaniu określonego adresu url
        found = resolve('/')
        self.assertEqual(found.func,home_page)