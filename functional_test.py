from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import unittest
import time



class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_late(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000') 

        # She notices the page title and header mention to-do lists
        self.assertIn('Django', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        # [..res of comments as before]


if __name__ == '__main__':
    unittest.main(warnings='ignore')


