from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

# Enter keyword to search
keyword_to_search = sys.argv[1]

# Validate search keyword entered
if keyword_to_search is None:
    print("No keyword to search")
    exit(1)

# Open the website
driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
time.sleep(4)

# Get input elements on page
page_input_elements = driver.find_elements(By.TAG_NAME, 'input')

# Finds search input element from input list of elements and send keyword_to_search to it
for element in page_input_elements:
    element_desc = element.get_attribute('aria-label')
    if 'Search' in str(element_desc):
        # Press Enter on Search Button
        element.send_keys(keyword_to_search)
        break

# Sleep for 5 sec to wait for whole page elements to be loaded
time.sleep(5)

#<input type="submit" class="btn btn-prim gh-spr" id="gh-btn" value="Search">
# Get input elements on page
page_button_elements = driver.find_elements(By.TAG_NAME, 'input')

# Find Search button from input list of elements and click on it
for element in page_button_elements:
    element_class = element.get_attribute('type')
    print(element_class)
    if 'submit' in str(element_class):
        # Click on Search Button
        element.send_keys(Keys.ENTER)
        break
