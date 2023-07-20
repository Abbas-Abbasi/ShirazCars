from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

##############################################################
# Create Firefox options
firefox_options = Options()

# Set the path to the Firefox binary (update with the correct path)
firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'

# Launch Firefox using geckodriver
driver = webdriver.Firefox(options=firefox_options)
##################################################################################
# To get the cookies and save them Only run 1 Time Then Comment them
# # Navigate to the Udemy login page
# driver.get("https://www.udemy.com/join/login-popup/")
# time.sleep(5)  # Adjust the delay as per your requirements
# time.sleep(5)  # Adjust the delay as per your requirements
# # Perform the login process (replace with your actual login code)
# email_input = driver.find_element(By.XPATH, '//*[@id="form-group--1"]')
# password_input = driver.find_element(By.XPATH, '//*[@id="form-group--3"]')
# login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/form/button/span")
#
# email_input.send_keys("i.erfanme@yahoo.com")  # Replace with your email
# password_input.send_keys("SjYXwg3baj")  # Replace with your password
# login_button.click()

# Wait for the login process to complete
time.sleep(5)  # Adjust the delay as per your requirements

time.sleep(5)  # Adjust the delay as per your requirements

#   Save Cookies
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

##################################################################################
#   Use Cookies
# driver.get("https://www.udemy.com/")
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
##################################################################################
# keyword = "href"
# driver.get("https://www.real.discount/free-online-courses/")
# try:
#     search_result = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.NAME,"a"))
#     time.sleep(20)
#     print("Search Result is as follows :", search_result)
# except:
#     # driver.quit()
#     pass
##################################################################################


##################################################################################
