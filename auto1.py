import csv
import random
from selenium import webdriver
from selenium import selenium
from colors import red, green, blue
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import thread

#initializing driver, and opening the webpage

# chrome_options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(
#     executable_path=r"c:\chromedriver.exe",
#     chrome_options=chrome_options)

profile = webdriver.FirefoxProfile()
profile.set_preference('network.http.phishy-userpass-length', 255)
driver = webdriver.Firefox(firefox_profile=profile)


# --------- login ssh
driver.get("http://admin:ckids@develop.ckids.web.drucode.com/")

# --------- login account "Centre administration"
username_editname = driver.find_element_by_id("edit-name")
passw_editpass = driver.find_element_by_id("edit-pass")
click_login = driver.find_element_by_id("edit-submit")
username_editname.send_keys("creche_admin")
passw_editpass.send_keys("creche_admin")
print green ('Login as: "creche_admin / creche_admin"')

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



#region------ ADD Children
print blue("Click link 'Children'")
driver.set_page_load_timeout(300)
children_link = driver.find_element_by_link_text("Children")
children_link.click()
driver.set_page_load_timeout(300)
add_new_child_link = driver.find_element_by_class_name("add-content-button")
add_new_child_link.click()

print blue("Creating child...")
# wait = WebDriverWait(driver, 10)
driver.set_page_load_timeout(300)
firstname_child = driver.find_element_by_id("edit-title")
firstname_child.send_keys("Children_first2")
lastname_child = driver.find_element_by_id("edit-field-child-second-name-und-0-value")
lastname_child.send_keys("Children_last2")
print green('Created child name: "Children_first2 / Children_last2"')

driver.set_page_load_timeout(40)
droproom = driver.find_element_by_id("edit-field-child-room-und")
flag = False
for option in droproom.find_elements_by_tag_name('option'):
    if option.text == 'Room #2': # now system has 3 rooms
        option.click()
        print green('You selected: ' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't  find Room")

dropsex = driver.find_element_by_id("edit-field-child-sex-und")
flag = False
for option in dropsex.find_elements_by_tag_name('option'):
    if option.text == 'Male': #or Female
        option.click()
        print green('You selected: ' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't find option sex")

dropphotos = driver.find_element_by_id("edit-field-child-photos-und")
flag = False
for option in dropphotos.find_elements_by_tag_name('option'):
    if option.text == 'Allowed': #or Not Allowed
        option.click()
        print green('You selected: ' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't find option photos")

autoallergies = driver.find_element_by_id("edit-field-child-allergies-und")
autoallergies.send_keys("Plums") #list of all allergies

add_new_family = driver.find_element_by_id("edit-field-child-family-und")
for option in add_new_family.find_elements_by_tag_name('option'):
  if option.text == '== Add New Family for this Child ==':
        option.click()
        print green('Add family: ' + option.text)


# save_changes = driver.find_element_by_id("edit-submit")
# save_changes.click()

driver.find_element_by_class_name("cancel-button").click()

#endregion children

#region------ ADD FAMILY
print blue("Click 'Family'")
driver.get("http://develop.ckids.web.drucode.com/node/add/family")

if driver.get == False:
    print ('Cant open this page' + driver.get)
driver.set_page_load_timeout(40)
firstname_family = driver.find_element_by_id("edit-title") # First name
firstname_family.send_keys("Parren_first1")
lastname = driver.find_element_by_id("edit-field-family-second-name-und-0-value") # Last name
lastname.send_keys("Parrent_last1")
email_family = driver.find_element_by_id("edit-field-family-email-und-0-email")
email_family.send_keys("testauto@gmail.com")
phone = driver.find_element_by_id("edit-field-family-phone-und-0-value")
phone.send_keys("+38090 9090908 09088080")
#---add parents / Guardians
firstname_gua = driver.find_element_by_id("edit-fgm-node-family-form-group-additional-parents-fields-items-0-field-family-addition-first-name-und-value") # First name
firstname_gua.send_keys("Guardians_first1")
lastname = driver.find_element_by_id("edit-fgm-node-family-form-group-additional-parents-fields-items-0-field-family-add-second-name-und-value") # Last name
lastname.send_keys("Guardians_last1")
phone = driver.find_element_by_id("edit-fgm-node-family-form-group-additional-parents-fields-items-0-field-family-addition-phone-und-value")
phone.send_keys("+3809809 808909 800 09")
#doesn't work "add another item button
# add_another_item = driver.find_elements_by_link_text("Add another item")
# add_another_item.click()

# # save_changes = driver.find_element_by_id("edit-submit")
# # save_changes.click()
link_cancel = driver.find_element_by_class_name("cancel-button")
link_cancel.click()

#endregion

#region ------ ADD Carer
print blue("Click 'Carer'")
driver.get("http://develop.ckids.web.drucode.com/node/add/carer")
driver.set_page_load_timeout(40)
print blue("Creating 'Carer'")
firstname_carer = driver.find_element_by_id("edit-title") # First name
firstname_carer.send_keys("Carer_first1")
lastname_carer = driver.find_element_by_id("edit-field-carer-second-name-und-0-value") # Last name
lastname_carer.send_keys("Carer_last1")
email_family = driver.find_element_by_id("edit-field-carer-email-und-0-email")
email_family.send_keys("testauto@gmail.com")

dropsexcarer = driver.find_element_by_id("edit-field-carer-sex-und")
flag = False
for option in dropsexcarer.find_elements_by_tag_name('option'):
    if option.text == 'Male': #or Female
        option.click()
        print green('You selected: ' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't find option sex")

print blue("Selecting photo...")
click_browse_carer = driver.find_element_by_id("edit-field-carer-photo-und-0-upload")
click_browse_carer.send_keys("D:\\stock-photo-woman-smiling-and-standing-in-the-front-of-the-computer-class-114470674.jpg")
driver.find_element_by_id("edit-field-carer-photo-und-0-upload-button").click()

print green("Added photo 'Carer'")
wait = WebDriverWait(driver, 10)
wait.until(lambda driver: driver.find_element_by_xpath("//*[@id='edit-field-carer-photo-und-0-remove-button']"))

droproom1 = driver.find_element_by_id("edit-field-carer-room-mon-und")
flag = False
for option in droproom1.find_elements_by_tag_name('option'):
    if option.text == 'Not Working':
        option.click()
        print green('You selected: "Mon"' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't find room: " + option.text)

droproom2 = driver.find_element_by_id("edit-field-carer-room-tue-und")
flag = False
for option in droproom2.find_elements_by_tag_name('option'):
    if option.text == 'Room #1':
        option.click()
        print green('You selected: "Tue"' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't find room: " + option.text)

droproom3 = driver.find_element_by_id("edit-field-carer-room-wed-und")
flag = False
for option in droproom3.find_elements_by_tag_name('option'):
    if option.text == 'Room #2':
        option.click()
        print green('You selected: "Wed"' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't find room: " + option.text)

droproom4 = driver.find_element_by_id("edit-field-carer-room-thu-und")
flag = False
for option in droproom4.find_elements_by_tag_name('option'):
    if option.text == 'Room #3':
        option.click()
        print green('You selected: "Thu"' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't find room: " + option.text)

droproom5 = driver.find_element_by_id("edit-field-carer-room-fri-und")
flag = False
for option in droproom5.find_elements_by_tag_name('option'):
    if option.text == 'Room #4':
        option.click()
        print green('You selected: "Fri"' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't find room: " + option.text)

droproom6 = driver.find_element_by_id("edit-field-carer-room-sat-und")
flag = False
for option in droproom6.find_elements_by_tag_name('option'):
    if option.text == 'Room #5':
        option.click()
        print green('You selected: "Sat"' + option.text)
        flag = True
if (flag != True):
   print red("Error. Can't find room: " + option.text)

droproom7 = driver.find_element_by_id("edit-field-carer-room-sun-und")
flag = False
for option in droproom7.find_elements_by_tag_name('option'):
    if option.text == 'Room #6':
        option.click()
        print green('You selected: "Sun"' + option.text)
        flag = True
if (flag != True):
    print red("Error. Can't find room: " + option.text)

# # # driver.find_element_by_id("edit-submit").click()

driver.find_element_by_class_name("cancel-button").click()

#endregion

# region ------ ADD Photo
print blue("Adding photo... Click 'Photos'")
driver.get("http://develop.ckids.web.drucode.com/centre/xyz-childrens-creche/photos")

driver.find_element_by_class_name("add-content-button").click()
wait.until(lambda driver: driver.find_element_by_xpath("//*[@id='edit-title']"))
title_photo = driver.find_element_by_id("edit-title")
title_photo.send_keys("test photo1")

print blue('selecting photo... ')
browse = driver.find_element_by_id("edit-field-photo-und-0-upload")
browse.send_keys("D:\\stock-photo-girl-with-bubbles-104648267.jpg")
driver.find_element_by_id("edit-field-photo-und-0-upload-button").click()

print green("Added photo")
wait = WebDriverWait(driver, 10)
wait.until(lambda driver: driver.find_element_by_xpath("//*[@id='edit-field-photo-und-0-ajax-wrapper']/div/div/div/div[1]/a/img"))
driver.get_screenshot_as_file("D:\\test2.png")
print green("Screenshot is created")

print blue("Finding child in photo...")
children_in_photo = driver.find_element_by_id("edit-field-photo-child-und")
flag2 = False
for option in children_in_photo.find_elements_by_tag_name('option'):
     if option.text == "Children_first2 Children_last2":
         option.click()
         print green('You selected: ' + option.text)
         flag2 = True
if (flag2 != True):
     print red("Error. Can't find children " + option.text)
# endregion Photo
