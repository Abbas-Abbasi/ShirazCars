from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pandas as pd

# Create Firefox options
firefox_options = Options()

# Set the path to the Firefox binary (update with the correct path)
firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'

# Launch Firefox using geckodriver
driver = webdriver.Firefox(options=firefox_options)

# Navigate to the Real Discount website
driver.get("https://www.real.discount/")

# Wait for the page to fully load
driver.implicitly_wait(10)  # Adjust the delay as per your requirements

# Get the page source
page_source = driver.page_source

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(page_source, "html.parser")

# Find the course links using BeautifulSoup
course_links = []
course_elements = soup.select("div.course-title a")
for element in course_elements:
    link = element["href"]
    course_links.append(link)

# Save the course links in an Excel file
df = pd.DataFrame({"Course Links": course_links})
df.to_excel("courseLinks.xlsx", index=False)

# Close the browser session
driver.quit()
