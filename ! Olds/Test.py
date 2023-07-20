from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# Create Firefox options
firefox_options = Options()

# Set the path to the Firefox binary (update with the correct path)
firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'

# Launch Firefox using geckodriver
driver = webdriver.Firefox(options=firefox_options)

# Navigate to the Udemy login page
driver.get("https://www.udemy.com/join/login-popup/")
time.sleep(5)  # Adjust the delay as per your requirements
time.sleep(5)  # Adjust the delay as per your requirements
# Perform the login process (replace with your actual login code)
email_input = driver.find_element(By.XPATH, '//*[@id="form-group--1"]')
password_input = driver.find_element(By.XPATH, '//*[@id="form-group--3"]')
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/form/button/span")

email_input.send_keys("i.erfanme@yahoo.com")  # Replace with your email
password_input.send_keys("SjYXwg3baj")  # Replace with your password
login_button.click()

# Wait for the login process to complete
time.sleep(5)  # Adjust the delay as per your requirements

time.sleep(5)  # Adjust the delay as per your requirements
time.sleep(5)  # Adjust the delay as per your requirements

# Rest of the code for your automation process...
# Add your logic to scrape Real Discount website, open course links, and enroll in courses

# Remember to handle exceptions, add appropriate delays, and handle CAPTCHA challenges if any

# Close the browser session
# driver.quit()
