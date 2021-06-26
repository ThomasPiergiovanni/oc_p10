from selenium import webdriver

from django.test import TestCase

class NewVisitorTest(TestCase):
    """
    """
    def setUp(self):
        self.browser = webdriver.Edge('C:\Program Files\EdgeDriver\msedgedriver.exe')
        # self.browser = webdriver.Edge()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_index_has_correct_title(self):
        self.browser.get('http://127.0.0.1:8000/supersub')
        self.assertIn("P8 - Pur-beurre", self.browser.title)

    def test_index_has_main_form(self):
        self.browser.get('http://127.0.0.1:8000/supersub/')
        self.browser.find_element_by_id('index_main_search_form')
    
    def test_index_has_search_button(self):
        self.browser.get('http://127.0.0.1:8000/supersub/')
        self.browser.find_element_by_id('index_search_button')

    def test_search_a_product_and_get_answer_back(self):
        pass
    