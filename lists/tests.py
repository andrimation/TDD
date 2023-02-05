from django.test import TestCase
# django.test -> to rozszeżona wersja unittest dla django !

# Create your tests here.

class SmokeTest(TestCase):

    def test_bad(self):
        self.assertEqual(1+1,3)