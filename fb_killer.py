#!/usr/bin/python
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException, WebDriverException


# Fill out these Variables
members_page = "" # url or your group/members example : https://www.facebook.com/groups/<your group number>/members
number_of_admins = 0 # If you leave this at 0, you will ban admins, including yourself
email = '' # for login
fb_passwd = "" for login


def get_members():

    driver.get(members_page)
    count = 0
    for c in driver.find_elements_by_class_name('sp_ytMFiRbN9O-'):
        count += 1
        print count
        if count < number_of_admins:
            continue

        try:
            c.click()
            elem = driver.find_elements_by_class_name('_54nh')
            elem[2].click()
            sleep(1)
            driver.find_element_by_class_name('uiInputLabelInput').click()
            sleep(1)
            driver.find_element_by_class_name('layerConfirm').click()
            sleep(5)
            get_members()
        except WebDriverException as e:
            print
            continue
        except NoSuchElementException:
            print "not found"


driver = webdriver.Firefox()
driver.get("https://www.facebook.com")
email_field = driver.find_element_by_id('email')
email_field.send_keys(email)
passwd_field = driver.find_element_by_id('pass')
passwd_field.send_keys(fb_passwd)
passwd_field.submit()

get_members()
