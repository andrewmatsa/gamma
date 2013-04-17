from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#initializing driver, and opening the webpage

profile = webdriver.FirefoxProfile()
profile.set_preference('network.http.phishy-userpass-length', 255)
driver = webdriver.Firefox(firefox_profile=profile)
driver.get("http://admin:ckids@develop.ckids.web.drucode.com/")


username_editname = driver.find_element_by_id("edit-name")
passw_editpass = driver.find_element_by_id("edit-pass")
click_login = driver.find_element_by_id("edit-submit")

username_editname.send_keys("ckids_admin")
passw_editpass.send_keys("ckids_admin")
click_login.click()
