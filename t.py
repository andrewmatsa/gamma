from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Browse(unittest.TestCase):
    def setUp(self):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    base_url = "http://careergrab.ionface.com/"

    filename = 'test.csv'
    line_number = 1
    with open(filename, 'rb') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        username=mycsv[line_number][0]
        password=mycsv[line_number][1]
        verificationErrors = []

def test_browse(self):
    driver = self.driver
    driver.get(self.base_url + "/")
    driver.find_element_by_css_selector("img[alt=\"img\"]").click()
    driver.find_element_by_link_text("Career Grab").click()
    driver.find_element_by_class_name("browse").click()
    driver.find_element_by_id("id_identification").clear()
    driver.find_element_by_id("id_identification").send_keys(self.username)
    for index in range(len(self.password)):
    driver.find_element_by_id("id_password").clear()
    driver.set_page_load_timeout
    driver.find_element_by_id("id_password").send_keys(self.password)
    driver.find_element_by_css_selector("input.login-button").click()

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True

def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)