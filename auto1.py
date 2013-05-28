import csv
import random
from selenium import webdriver
from colors import red, green, blue
from selenium.webdriver.common.keys import Keys

#initializing driver, and opening the webpage

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    executable_path=r"c:\chromedriver.exe",
    chrome_options=chrome_options)


# some comment
# profile = webdriver.FirefoxProfile()
# profile.set_preference('network.http.phishy-userpass-length', 255)
# driver = webdriver.Firefox(firefox_profile=profile)


# --------- login ssh
driver.get("http://admin:ckids@develop.ckids.web.drucode.com/")

# --------- login account "Centre administration"
username_editname = driver.find_element_by_id("edit-name")
passw_editpass = driver.find_element_by_id("edit-pass")
click_login = driver.find_element_by_id("edit-submit")
username_editname.send_keys("creche_admin")
passw_editpass.send_keys("creche_admin")

# f = open("C:\\test.csv", 'rt')
# names = []
# surnames = []
# try:
#     reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
#     for row in reader:
#         names.append(row[0])
#         surnames.append(row[1])
#     username_editname.send_keys(names[random.randint(0, names.__len__() - 1)])
#     # surnames.send_keys(surnames[2])
#     passw_editpass.send_keys(surnames[random.randint(0, names.__len__() - 1)])
#     # field4.send_keys(somenumbers[random.randint(0, names.__len__() - 1)])
# finally:
#     f.close()
click_login.click()

#------ADD Children
driver.set_page_load_timeout(40)
children_link = driver.find_element_by_link_text("Children")
children_link.click()
driver.set_page_load_timeout(30)
add_new_child_link = driver.find_element_by_class_name("add-content-button")
add_new_child_link.click()

driver.set_page_load_timeout(30)
firstname = driver.find_element_by_id("edit-title") # First name
firstname.send_keys("Children_first1")
lastname = driver.find_element_by_id("edit-field-child-second-name-und-0-value") # Last name
lastname.send_keys("Children_last1")
#
driver.set_page_load_timeout(40)
droproom = driver.find_element_by_id("edit-field-child-room-und")
flag = False
for option in droproom.find_elements_by_tag_name('option'):
    if option.text == 'Room #2': # now system has 3 rooms
        option.click()
        print ('You selected: ' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't  find Room")

dropsex = driver.find_element_by_id("edit-field-child-sex-und")
flag = False
for option in dropsex.find_elements_by_tag_name('option'):
    if option.text == 'Male': #or Female
        option.click()
        print ('You selected: ' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't find option sex")

dropphotos = driver.find_element_by_id("edit-field-child-photos-und")
flag = False
for option in dropphotos.find_elements_by_tag_name('option'):
    if option.text == 'Allowed': #or Not Allowed
        option.click()
        print ('You selected: ' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't find option photos")

autoallergies = driver.find_element_by_id("edit-field-child-allergies-und")
autoallergies.send_keys("Plums") #list of all allergies

add_new_family = driver.find_element_by_id("edit-field-child-family-und")
for option in add_new_family.find_elements_by_tag_name('option'):
  if option.text == '== Add New Family for this Child ==':
        option.click()
        print ('Add family: ' + option.text)


# save_changes = driver.find_element_by_id("edit-submit")
# save_changes.click()

link_cancel = driver.find_element_by_class_name("cancel-button")
link_cancel.click()
#
# #---- ADD FAMILY
# driver.get("http://develop.ckids.web.drucode.com/node/add/family")
#
# if driver.get == False:
#     print ('Cant open this page' + driver.get)
# driver.set_page_load_timeout(40)
# firstname = driver.find_element_by_id("edit-title") # First name
# firstname.send_keys("Parren_first1")
# lastname = driver.find_element_by_id("edit-field-family-second-name-und-0-value") # Last name
# lastname.send_keys("Parrent_last1")
# email_family = driver.find_element_by_id("edit-field-family-email-und-0-email")
# email_family.send_keys("testauto@gmail.com")
# phone = driver.find_element_by_id("edit-field-family-phone-und-0-value")
# phone.send_keys("+38090 9090908 09088080")
# #---add parents / Guardians
# firstname = driver.find_element_by_id("edit-fgm-node-family-form-group-additional-parents-fields-items-0-field-family-addition-first-name-und-value") # First name
# firstname.send_keys("Guardians_first1")
# lastname = driver.find_element_by_id("edit-fgm-node-family-form-group-additional-parents-fields-items-0-field-family-add-second-name-und-value") # Last name
# lastname.send_keys("Guardians_last1")
# phone = driver.find_element_by_id("edit-fgm-node-family-form-group-additional-parents-fields-items-0-field-family-addition-phone-und-value")
# phone.send_keys("+3809809 808909 800 09")
# #doesn't work "add another item button
# # add_another_item = driver.find_elements_by_link_text("Add another item")
# # add_another_item.click()
#
# # # save_changes = driver.find_element_by_id("edit-submit")
# # # save_changes.click()
# link_cancel = driver.find_element_by_class_name("cancel-button")
# link_cancel.click()
#
#
# #---- ADD Carer
# driver.get("http://develop.ckids.web.drucode.com/node/add/carer")
# driver.set_page_load_timeout(40)
# firstname = driver.find_element_by_id("edit-title") # First name
# firstname.send_keys("Carer_first1")
# lastname = driver.find_element_by_id("edit-field-carer-second-name-und-0-value") # Last name
# lastname.send_keys("Carer_last1")
# email_family = driver.find_element_by_id("edit-field-carer-email-und-0-email")
# email_family.send_keys("testauto@gmail.com")
#
# dropsexcarer = driver.find_element_by_id("edit-field-carer-sex-und")
# flag = False
# for option in dropsexcarer.find_elements_by_tag_name('option'):
#     if option.text == 'Male': #or Female
#         option.click()
#         print ('You selected: ' + option.text)
#         flag = True
# if (flag != True):
#     print ("Error. Can't find option sex")
#
# # photocarer = driver.find_element_by_id("edit-field-carer-photo-und-0-upload")
# # photocarer.click()
# # driver.findElement(By.xpath("//div[text()='Upload Photos/Video']following-sibling::div/input")).sendKeys("C:\\MyPhoto.jpg");
# # driver.find_element_by_id("edit-field-carer-photo-und-0-upload").sendKeys("D:/stock-photo-boys-and-girls-running-towards-ball-59018779.jpg")
#
# droproom = driver.find_element_by_id("edit-field-carer-room-mon-und")
# flag = False
# for option in droproom.find_elements_by_tag_name('option'):
#     if option.text == 'Not Working':
#         option.click()
#         print ('You selected: ' + option.text)
#         flag = True
# if (flag != True):
#     print ("Error. Can't find room: " + option.text)
#
# droproom = driver.find_element_by_id("edit-field-carer-room-tue-und")
# flag = False
# for option in droproom.find_elements_by_tag_name('option'):
#     if option.text == 'Room #1':
#         option.click()
#         print ('You selected: ' + option.text)
#         flag = True
# if (flag != True):
#     print ("Error. Can't find room: " + option.text)
#
# droproom = driver.find_element_by_id("edit-field-carer-room-wed-und")
# flag = False
# for option in droproom.find_elements_by_tag_name('option'):
#     if option.text == 'Room #2':
#         option.click()
#         print ('You selected: ' + option.text)
#         flag = True
# if (flag != True):
#     print ("Error. Can't find room: " + option.text)
#
# droproom = driver.find_element_by_id("edit-field-carer-room-thu-und")
# flag = False
# for option in droproom.find_elements_by_tag_name('option'):
#     if option.text == 'Room #3':
#         option.click()
#         print ('You selected: ' + option.text)
#         flag = True
# if (flag != True):
#     print ("Error. Can't find room: " + option.text)
#
# droproom = driver.find_element_by_id("edit-field-carer-room-fri-und")
# flag = False
# for option in droproom.find_elements_by_tag_name('option'):
#     if option.text == 'Room #4':
#         option.click()
#         print ('You selected: ' + option.text)
#         flag = True
# if (flag != True):
#     print ("Error. Can't find room: " + option.text)
#
# droproom = driver.find_element_by_id("edit-field-carer-room-sat-und")
# flag = False
# for option in droproom.find_elements_by_tag_name('option'):
#     if option.text == 'Room #5':
#         option.click()
#         print ('You selected: ' + option.text)
#         flag = True
# if (flag != True):
#    print ("Error. Can't find room: " + option.text)
#
# droproom = driver.find_element_by_id("edit-field-carer-room-sun-und")
# flag = False
# for option in droproom.find_elements_by_tag_name('option'):
#     if option.text == 'Room #6':
#         option.click()
#         print ('You selected: ' + option.text)
#         flag = True
# if (flag != True):
#     print ("Error. Can't find room: " + option.text)
#
# # # # save_changes = driver.find_element_by_id("edit-submit")
# # # # save_changes.click()
# link_cancel = driver.find_element_by_class_name("cancel-button")
# link_cancel.click()