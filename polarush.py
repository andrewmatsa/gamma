#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import unittest, time


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://translate.google.com/")

    def tearDown(self):
        self.driver.quit()

    def choose_language(self, menu, lang):
        driver = self.driver
        _from = {
                 "button":{"by":By.ID, "value":"gt-sl-gms"},
                 "menu":{"by":By.ID, "value":"gt-sl-gms-menu"},
                 "lang":{"by":By.XPATH, "value":"//*[@class='goog-menuitem-content'][contains(text(), '%s')]" % lang},
        }
        _to = {
                 "button":{"by":By.ID, "value":"gt-tl-gms"},
                 "menu":{"by":By.ID, "value":"gt-tl-gms-menu"},
                 "lang":{"by":By.XPATH, "value":"//div[@id ='gt-tl-gms-menu']//*[@class='goog-menuitem-content'][contains(text(), '%s')]" % lang},
        }
        context = _from if menu == "from" else _to
        button = driver.find_element(**context['button'])
        button.click()
        menu = driver.find_element(**context['menu'])
        WebDriverWait(driver, 10).until(lambda d: d.find_element(**context['menu']))
        lang = menu.find_element(**context['lang'])
        lang.click()

    def translate_text(self, *text):
        driver = self.driver
        source = driver.find_element_by_id("source")
        for word in text:
            source.send_keys(word + Keys.ENTER)
        result = driver.find_element_by_id("result_box")
        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements_by_xpath("//*[@id='result_box']/span")) >= len(text))
        return result.text

class TestTranslation(BaseTestCase):

    def test_translation_with_drag_and_drop_in_results(self):
        driver = self.driver
        self.choose_language("from", "Detect language")
        self.choose_language("to", "English")
        result = self.translate_text(u"и",
                                     u"пусть",
                                     u"будет автоматизация всегда",
                                     u"http://poliarush.com"
                                     )
        self.assertIn("and", result)

if __name__ == "__main__":
    unittest.main()