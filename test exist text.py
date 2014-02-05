import unittest
from selenium import webdriver


class Selenium2OnLocal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_from_local(self):
        self.driver.get("http://admin:dr@develop.dr.web.drucode.com")
        # self.assertEqual('I am a page title - Sauce Labs', self.driver.title)
        body = self.driver.find_element_by_css_selector('body')
        f = self.assertIn('Welcome to Dr5ucode. Be our guest and take a tour of what we do.', body.text)

    def tearDown(self):
        self.driver.quit()


        # http://software-testing.ru/forum/index.php?/topic/20955/