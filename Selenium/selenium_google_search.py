from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# Download Chrome Driver
# https://chromedriver.chromium.org/downloads

# Get current working directory
cwd = os.getcwd()
cdp = cwd + "\chromedriver.exe"

# set chromodriver.exe path
#driver = webdriver.Chrome(executable_path=cdp)
driver.implicitly_wait(0.5)

# launch URL
driver.get("https://www.google.com/")

# identify search box
#m = driver.find_element_by_name("q") - before selenium 4.3.0 - https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el
m = driver.find_element(By.NAME, "q")

# enter search text
m.send_keys("selenium")
time.sleep(0.2)

#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)
