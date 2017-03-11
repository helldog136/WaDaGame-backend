from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

driver = webdriver.Chrome()
#driver.get("https://www.google.com/imghp?hl=en")
driver.get("https://ctrlq.org/google/images/")

# Click "Search by image" icon
#elem = driver.find_element_by_id('uploadbtn')
#elem = driver.find_element_by_id('uploadbtn')
#elem.click()
#elem = login_wait.until(EC.visibility_of_element_located((By.ID, 'uploadbtn')))
#driver.find_element_by_css_selector('input[type="file"]').clear()
#elem.send_keys(os.getcwd()+"/Users/nicolaspotie/Desktop/studentHackImage/ftl01.jpg")
#elem.click()
#driver.find_element_by_id('uploadbtn').clear()
time.sleep(10)
driver.find_element_by_id('uploadbtn').send_keys("/Users/nicolaspotie/Desktop/studentHackImage/ftl01.jpg")
#elem.send_keys("/Users/nicolaspotie/Desktop/studentHackImage/ftl01.jpg")

#elem = driver.find_element_by_class_name("dropzone hidden")
#elem.send_keys("ftl01.jpg")
# Switch from "Paste image URL" to "Upload an image"
#driver.execute_script("google.qb.ti(true);return false")
# Set the path of the local file and submit

#elem = driver.find_element_by_id("qbfile")
#elem.send_keys("/Users/nicolaspotie/Desktop/studentHackImage/ftl01.jpg")

#ele1 = driver.find_element_by_class_name("gbqfb kpbb")
#ele1 = driver.find_element_by_link_text("Search by image")
#ele1.click()

