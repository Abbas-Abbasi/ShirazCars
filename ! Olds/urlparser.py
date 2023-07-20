from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Create Firefox options
firefox_options = Options()

# Set the path to the Firefox binary (update with the correct path)
firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'

# Launch Firefox using geckodriver
driver = webdriver.Firefox(options=firefox_options)

# Navigate to the Real Discount website
driver.get("https://www.real.discount/free-online-courses/")

# Wait for the page to fully load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.udlite-heading-md")))

# Get the page source
html = driver.page_source

# Create a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find all the course links
course_links = []
link_elements = soup.find_all("a")
for element in link_elements:
    href = element.get("href")
    if href and href.startswith("https://www.udemy.com/"):
        course_links.append(href)
        print(href)

# Close the browser session
driver.quit()
