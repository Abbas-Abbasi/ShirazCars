import logging
import csv
import time
from selenium import webdriver
# from loginUdemy import UdemyLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, TimeoutException
import pickle


################################################################################################################

class UdemyEnroll:
    def __init__(self):
        self.driver = None
        self.wait = None

    ############# Setup Driver
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
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/114.0.0.0 Safari/537.36'
        chrome_options.add_argument(f"--user-agent={user_agent}")
        # Add the option to start Chrome maximized
        chrome_options.add_argument("--start-maximized")
        # Launch Chrome using chromedriver
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 50)

    ############# Open Links In new Tabs
    def open_links_in_tabs(self, links):
        for link in links:
            self.driver.execute_script("window.open('about:blank', '_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(link)

    ############# Enroll in Courses
    def enroll_courses(self, links):
        for link in links:
            FreeXPath = '//span[text()="Free"]'
            EnrollXPath = '//button/span[text()="Enroll now"]'
            GoToCourseXPath = '//button/span[text()="Go to course"]'

            self.driver.execute_script("window.open('about:blank', '_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(link)

            if FreeXPath and EnrollXPath:
                try:
                    self.wait.until(EC.presence_of_element_located((By.XPATH, FreeXPath)))
                    self.wait.until(EC.presence_of_element_located((By.XPATH, EnrollXPath)))
                    self.driver.find_element(By.XPATH, EnrollXPath).click()
                except NoSuchElementException:
                    # Handle NoSuchElementException (Element not found)
                    print("Enroll button not found. Skipping enrollment.")
                except Exception as e:
                    # Handle any other unexpected exceptions
                    print(f"An unexpected error occurred: {str(e)}")

            elif GoToCourseXPath:
                try:
                    self.wait.until(EC.presence_of_element_located((By.XPATH, GoToCourseXPath)))

                    self.driver.find_element(By.XPATH, GoToCourseXPath)
                    # Add the link to alreadyEnrolled.csv
                    with open('alreadyEnrolled.csv', 'a') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([link])
                except NoSuchElementException:
                    # Handle NoSuchElementException (Element not found)
                    print("Go to course button not found. Skipping link addition.")
                except Exception as e:
                    # Handle any other unexpected exceptions
                    print(f"An unexpected error occurred: {str(e)}")

            else:
                continue

    ############# Load Cookies
    def load_cookies(self, sites):
        self.driver.get(sites)
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # is_logged_element = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/a/span'
        # self.wait.until(EC.presence_of_element_located((By.XPATH, is_logged_element)))

    ############# Close Browser
    def close_browser(self):
        self.driver.quit()


################################################################################################################


################################################################################################################

opener = UdemyEnroll()
opener.setup_driver()
url = "https://www.udemy.com/"
opener.load_cookies(url)
################################################################################################################

# Read the links from the CSV file
course_links = []
with open('courses_links.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        link = row[0]  # Assuming the link is in the first column of the CSV file
        course_links.append(link)

opener.enroll_courses(course_links)

# Close the browser after opening all links
opener.close_browser()
################################################################################################################
