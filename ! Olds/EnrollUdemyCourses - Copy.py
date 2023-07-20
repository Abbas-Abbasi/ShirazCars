from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle


####################################################################################################
class UdemyScraper:
    def __init__(self):
        self.driver = None
        self.wait = None

    def setup_driver(self):
        # Create Firefox options
        firefox_options = Options()
        # Set the path to the Firefox binary (update with the correct path)
        firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        # Launch Firefox using geckodriver
        self.driver = webdriver.Firefox(options=firefox_options)
        self.wait = WebDriverWait(self.driver, 100)

    def login(self, email, password):
        # Navigate to the Udemy login page
        self.driver.get("https://www.udemy.com/join/login-popup/")
        time.sleep(10)  # Adjust the delay as per your requirements
        # Perform the login process (replace with your actual login code)
        email_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-group--1"]')))
        password_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-group--3"]')))
        login_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/form/button/span")))

        email_input.send_keys(email)  # Replace with your email
        password_input.send_keys(password)  # Replace with your password
        login_button.click()

        # Wait for the login process to complete
        time.sleep(10)  # Adjust the delay as per your requirements

    def save_cookies(self):
        is_logged_element = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/a/span'
        self.wait.until(EC.presence_of_element_located((By.XPATH, is_logged_element)))
        # Save Cookies
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

        time.sleep(5)  # Adjust the delay as per your requirements

    def load_cookies(self, sites):
        self.driver.get(sites)
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        is_logged_element = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/a/span'
        self.wait.until(EC.presence_of_element_located((By.XPATH, is_logged_element)))

    def close_driver(self):
        self.driver.quit()


####################################################################################################
##################################### Example usage ################################################
##################### Example usage Setup an Instance of the Class #################################
scraper = UdemyScraper()
####################################################################################################
############################### Example usage Setup The Driver #####################################
scraper.setup_driver()
##############################  Login with Username and Password ###################################
# scraper.login("i.erfanme@yahoo.com", "SjYXwg3baj")
# time.sleep(5)  # Adjust the delay as per your requirements
############################### Example usage Save the Cookies #####################################
# scraper.save_cookies()
############################### Example usage Load the Cookies #####################################
url = "https://www.udemy.com/"
scraper.load_cookies(url)
# ... Perform further actions with the logged-in session ...
scraper.close_driver()

####################################################################################################
