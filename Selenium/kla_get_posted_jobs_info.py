# Script is searching for open positions posted at  KLA Careers website and print related jobs titles and it's url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
job_title_keyword = 'devops'


# Set the web driver to use Chrome
driver = webdriver.Chrome()

# Navigate to the login page of the Cloudera web UI
driver.get("https://klacareers.kla-tencor.com")

time.sleep(4)

# Enter job_title_keyword to search text field
search_jobs_text_field = driver.find_elements(By.TAG_NAME, 'input')
search_jobs_text_field[0].send_keys(job_title_keyword)

# Get page buttons into list
page_button_elements = driver.find_elements(By.TAG_NAME, 'button')

# Finds search button from button list of elements and press on it with enter
for element in page_button_elements:
    button_name = element.get_attribute('data-automation-id')
    if 'keywordSearchButton' in str(button_name):
        # Press Enter on Search Button
        element.send_keys(Keys.ENTER)
        break

time.sleep(4)

# Find all of the search result elements
result_elements = driver.find_elements(By.TAG_NAME,'a')

# Print the posted job titles and it's link from the search results
for element in result_elements:
    job_title = element.get_attribute('data-automation-id')
    if 'jobTitle' in str(job_title):
        job_url = element.get_attribute('href')
        print(str(element.text) + '        ' + str(job_url))

# Close chrome browser
driver.quit()
