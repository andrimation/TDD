from django.http import HttpRequest
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

    def test_home_page_returns_correct_thml(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Lista rzeczy do zrobienia</title>',response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        # response.content nie jest stringiem, dlatego żeby użyć porównywania
        # czy sprawdzenia, tekst sprawdzany,musi być zamieniony na bajty
        # b'<html>' - czyli w formacie bajtów, a nie unicode