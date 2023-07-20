import logging
import csv
import time
from selenium import webdriver
from loginUdemy import UdemyLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, TimeoutException


class UdemyEnroll:
    def __init__(self):
        self.driver = None
        self.wait = None

    def setup_driver(self):
        # Create Chrome options
        chrome_options = Options()
        # Set the path to the Chrome binary (update with the correct path)
        chrome_options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        # Set custom headers
        headers = {
            'Accept-Language': 'en-US,en;q=0.9',
            'Custom-Header': 'Value',
        }
        chrome_options.add_argument(f"--headers={headers}")

        # Set custom user agent
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        chrome_options.add_argument(f"--user-agent={user_agent}")
        # Add the option to start Chrome maximized
        chrome_options.add_argument("--start-maximized")
        # Launch Chrome using chromedriver
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 50)

    def load_cookies(self, url):
        self.driver.get(url)
        # Add code to load cookies

    def reload_page(self):
        self.driver.refresh()

    def close_browser(self):
        self.driver.quit()

    def enroll_courses(self, links):
        for link in links:
            self.driver.execute_script("window.open('about:blank', '_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(link)

            while True:
                try:
                    enroll_button = self.wait.until(
                        EC.presence_of_element_located((By.XPATH, '//button/span[text()="Go to course"]')))
                    enroll_button.click()
                    break
                except (NoSuchElementException, TimeoutException):
                    # Elements not found, reload the page
                    self.reload_page()

            # Check if the page is still not working after reloading
            if not self.check_elements_present():
                # Close the browser and open it again
                self.close_browser()
                self.setup_driver()
                self.load_cookies("https://www.udemy.com/")
                continue

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    def check_elements_present(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//button/span[text()="Go to course"]')))
            return True
        except (NoSuchElementException, TimeoutException):
            return False


# Usage
scraper = UdemyEnroll()
scraper.setup_driver()
scraper.load_cookies("https://www.udemy.com/")

# Read the links from the CSV file
course_links = []
with open('courses_links.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        link = row[0]  # Assuming the link is in the first column of the CSV file
        course_links.append(link)

scraper.enroll_courses(course_links)
