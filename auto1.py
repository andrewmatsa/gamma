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

username_editname.send_keys("creche_admin")
passw_editpass.send_keys("creche_admin")
click_login.click()

# Creating Children
driver.set_page_load_timeout(30)
children_link = driver.find_element_by_link_text("Children")
children_link.click()
driver.set_page_load_timeout(30)
add_new_child_link = driver.find_element_by_class_name("add-content-button")
add_new_child_link.click()

# firstname = driver.find_element_by_class_name("form-text required") #First name
# lastname = driver.find_element_by_class_name("text-full form-text") # Last name
driver.set_page_load_timeout(30)
droproom = driver.find_element_by_class_name("form-select")
for option in droproom.find_elements_by_tag_name('option'):
    if option.text == 'Room #3':
        option.click()
        print ('You selected:')
    else:
        print ('Error: No rooms in this centre!')


# driver.find_element("14")#room2
# driver.find_element("15")#room3
#room
#sex
#photos
#alergies autocomplete
#family
#buttom "save"

