from re import search
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import os
import time

def config_driver():
     PATH = "/home/simone/Documents/Code/SmartCampus_Bot/chromedriver_linux64/chromedriver"
     driver = webdriver.Chrome(PATH)
     return driver
def sign_in(driver):

     # vado sul sito di smartcampus
     driver.get("https://smartcampus.unical.it/student")
     driver.implicitly_wait(5)


     # 1 - seleziono il pulsante che rimanda alla pagina di login
     driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/a[1]").click()
     driver.implicitly_wait(5)

     # 2 - inserisco Username e Password  -- TODO: prenderla da Excel
     USR = "yourcf"; PSW = "yourpsw"

     driver.find_element_by_id("id_username").send_keys(USR)
     driver.find_element_by_id("id_password").send_keys(USR)
     driver.implicitly_wait(5)

     # 3tmp - dimentico l'accesso
     driver.find_element_by_xpath("/html/body/div/div/div[1]/div/form/div[4]/label").click()

     # 3 - accedo
     driver.find_element_by_class_name("btn").click()
     driver.implicitly_wait(5)



# main
driver = config_driver()
sign_in(driver)

# !!! test here !!!