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

time.sleep(1)

# Click on Login button
login_button = driver.find_element(By.NAME,'submit')
login_button.click()

# Click on Cluster drop down menu
cluster_drop_down_button = driver.find_element(By.CLASS_NAME,'cluster-drop-down')
cluster_drop_down_button.click()

# Click on Restart Button from drop down menu
restart_button = cluster_drop_down_button.find_element(By.PARTIAL_LINK_TEXT,'Restart')
restart_button.click()

# Wait for 2 seconds to load the webpage completely
time.sleep(2)

# Click Yes to confirm cluster restart
confirm_restart_button = restart_button.find_element(By.XPATH, '//button[text()="Restart"]')
confirm_restart_button.click()

# Sleep 5 min
time.sleep(300)

# Close Chrome browser
driver.quit()
