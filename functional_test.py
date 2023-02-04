from selenium import webdriver
import unittest




class NewVisitorTest(unittest.TestCase):

    def setUp(self):  # Metoda wykonywana przed wykonaniem właściwego testu
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3) # wymusza zaczekanie przeglądarki ( np żeby strona się załadowała )

    def tearDown(self): # Metoda wykonywana po wykonaniu własciwego testu
        self.browser.quit()

    # !! każda metoda w klasie unittest.TestCase, jeśli zaczyna się od test_ zostanie uznana za metode testową i wykonaną !!
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edyta dowiedziała się o nowej, wspaniałej aplikacji w postaci listy rzeczy do zrobienia.
        # Postanowiła więc przejść na stronę główną tej aplikacji
        self.browser.get('http://127.0.0.1:8000/')

        # Zwróciła uwagę, że tytuł strony i nagłówek zawierają słowo Listy.
        self.assertIn("Listy",self.browser.title)
        self.fail("Zakończenie testu!")

    # Od razu zostaje zachęcona aby wpisać rzeczy do zrobienia

    # W polu tekstowym wpisała "Kupić pawie pióra" ( hobby Edyty to tworzenie ozdób )

    # Po naciśnięciu klawisza "Enter" lista została uaktualniona, i wyświetla
    # "1: Kupić pawie pióra" jako element listy rzeczy do zrobienia

    # Na stronie nadal znajduje się pole tekstowe zachęcająco do podania kolejnej rzeczy
    # do zrobienia. Edyta wpisała "Użyć pawich piór do zrobienia przynęty"

    # Strona została ponownie uaktualniona i wyświetla dwa elementy na liście rzeczy do zrobienia

    # Edyta była ciekawa czy witryna zapamięta jej listę. Zwróciła uwagę na wygenerowany dla niej unikatowy
    # adres URL, obok którego znajduje się pewien tekst z wyjaśnieniem

    # Przechodzi pod podany adres  URL i widzi wyświetloną swoją listę rzeczy do zrobienia

    # Usatysfakcjonowana kładzie się spać


if __name__ == '__main__':
    unittest.main(warnings='ignore')


