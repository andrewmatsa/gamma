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
driver.set_page_load_timeout(40)
children_link = driver.find_element_by_link_text("Children")
children_link.click()
driver.set_page_load_timeout(30)
add_new_child_link = driver.find_element_by_class_name("add-content-button")
add_new_child_link.click()

driver.set_page_load_timeout(10)
firstname = driver.find_element_by_id("edit-title") # First name
firstname.send_keys("test_first_name")
lastname = driver.find_element_by_id("edit-field-child-second-name-und-0-value") # Last name
lastname.send_keys("test_last_name")

driver.set_page_load_timeout(40)
droproom = driver.find_element_by_id("edit-field-child-room-und")
flag = False
for option in droproom.find_elements_by_tag_name('option'):
    if option.text == 'Room #2': # now system has 3 rooms
        option.click()
        print ('You selected: ' + option.text)
        flag = True
if (flag != True):
    print ("Error. Can't  find Room")

dropsex = driver.find_element_by_id("edit-field-child-sex-und")
flag = False
for option in dropsex.find_elements_by_tag_name('option'):
    if option.text == 'Male': #or Female
        option.click()
        print ('You selected: ' + option.text)
        flag = True
if (flag != True):
    print ("Error. Can't find option sex")

dropphotos = driver.find_element_by_id("edit-field-child-photos-und")
flag = False
for option in dropphotos.find_elements_by_tag_name('option'):
    if option.text == 'Allowed': #or Not Allowed
        option.click()
        print ('You selected: ' + option.text)
        flag = True
if (flag != True):
    print ("Error. Can't find option photos")

autoallergies = driver.find_element_by_id("edit-field-child-allergies-und")
autoallergies.send_keys("plums") #list of all allergies






# save_changes = driver.find_element_by_id("edit-submit")
# save_changes.click()

