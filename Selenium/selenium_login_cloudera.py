from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Cloudera web server
cloudera_url = 'http://<NN1 IP Address>:7180/cmf/login'

# Cloudera user admin credentials
username = ''
password = ''

# Set the web driver to use Chrome
driver = webdriver.Chrome()

# Navigate to the login page of the Cloudera web UI
driver.get(cloudera_url)

# Find the username and password input fields and enter your credentials
username_input = driver.find_element(By.ID,'username')
username_input.send_keys(username)

password_input = driver.find_element(By.ID,'password')
password_input.send_keys(password)

time.sleep(3)

# Click on Login button
login_button = driver.find_element(By.NAME,'submit')
login_button.click()

time.sleep(15)

# Close chrome browser
driver.quit()
