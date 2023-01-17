# Script is searching for open positions posted at careers.google.com website and print related jobs titles and it's url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
job_title_keyword = 'devops'

# Set the web driver to use Chrome
driver = webdriver.Chrome()

# Navigate to the login page of the Cloudera web UI
driver.get("https://careers.google.com/jobs/results/?location=Israel")

# Send job_title_keyword argument to search input text field and Press Enter
search_jobs_text_field_input = driver.find_element(By.CLASS_NAME, 'gc-traditional-input')
search_jobs_text_field_input.send_keys(job_title_keyword)
search_jobs_text_field_input.send_keys(Keys.ENTER)

# Wait for the search results to be visible
search_results = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'search-results')))

# Find all of the search result elements
result_elements = search_results.find_elements(By.CLASS_NAME,'gc-card')

# Print the posted job titles and it's link from the search results
for element in result_elements:
    job_title = element.get_attribute('aria-label')
    job_url = element.get_attribute('href')
    print(str(job_title) + '        ' + str(job_url))

# Close chrome browser
driver.quit()