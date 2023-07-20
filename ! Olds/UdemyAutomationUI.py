import csv
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from loginUdemy import UdemyLogin
from getCourseLinks import UdemyCourseScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, TimeoutException


class UdemyAutomationUI:
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

    def enroll_courses(self, links):
        wait = WebDriverWait(self.driver, 50)
        for link in links:
            self.driver.execute_script("window.open('about:blank', '_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(link)

            enroll_button = wait.until(
                EC.presence_of_element_located((By.XPATH, '//button/span[text()="Go to course"]')))
            enroll_button.click()

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])


def run_scraper():
    # Read options from UI elements
    selected_website = website_combobox.get()
    num_pages = int(num_pages_entry.get())
    use_cookies = use_cookies_var.get()
    custom_user_agent = user_agent_entry.get()
    custom_headers = headers_entry.get()

    # Set the appropriate configurations based on the selected website
    if selected_website == "Website 1":
        linkElementXPath = '//*[@id="myList"]/li/a'
        nextButtonXPath = '//*/div/div/div[2]/div[3]/input'
        getCouponBtnXPATH = '/html/body/div[2]/div/div[2]/div[3]/div/a'
        website = "https://www.real.discount/free-online-courses/"
    elif selected_website == "Website 2":
        linkElementXPath = '//*[@id="coupon-page"]/div/div/div[1]/div/div/div/div[1]/h4/a'
        nextButtonXPath = '//*[@id="coupon-page"]/div/div/div[1]/ul/li[8]/a'
        getCouponBtnXPATH = '//*[@id="coupon-page"]/div/div/div[1]/div/div/div[3]/div/a'
        website = "https://udemyfreebies.com/"
    else:
        # Add more website configurations as needed
        return

    # Configuration for logging in to Udemy
    email = "your_email@example.com"
    password = "your_password"
    login_url = "https://www.udemy.com/"

    # Setup Udemy login scraper
    login_scraper = UdemyLogin()
    login_scraper.setup_driver()
    if use_cookies:
        login_scraper.load_cookies(login_url)
    else:
        login_scraper.login(email, password)
        login_scraper.save_cookies()

    # Setup Udemy course scraper
    course_scraper = UdemyCourseScraper(linkElementXPath, nextButtonXPath, getCouponBtnXPATH, website)
    course_scraper.setup_driver()
    course_scraper.set_custom_user_agent(custom_user_agent)
    course_scraper.set_custom_headers(custom_headers)
    course_scraper.load_cookies(login_url)
    course_scraper.scrape_links_load_more(num_pages)
    course_links = course_scraper.get_course_links()
    course_scraper.close_driver()

    # Enroll in the courses
    enroller = UdemyAutomationUI()
    enroller.setup_driver()
    enroller.load_cookies(login_url)
    enroller.enroll_courses(course_links)
    enroller.close_driver()

    # Alternatively, save the course links to a CSV file for later enrollment
    with open('courses_links.csv', 'w', newline='', encoding='UTF8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([[link] for link in course_links])
    print(f"Total unique links: {len(course_links)}")

    # Close the login driver
    login_scraper.close_driver()

# # Create the UI window
# window = tk.Tk()
# window.title("Udemy Automation")
# window.geometry("400x300")
#
# # Website Selection
# website_label = tk.Label(window, text="Select Website:")
# website_label.pack()
# website_combobox = ttk.Combobox(window, values=["Website 1", "Website 2"])
# website_combobox.current(0)
# website_combobox.pack()
#
# # Number of Pages
# num_pages_label = tk.Label(window, text="Number of Pages:")
# num_pages_label.pack()
# num_pages_entry = ttk.Entry(window)
# num_pages_entry.insert(tk.END, "3")
# num_pages_entry.pack()
#
# # Use Cookies Checkbox
# use_cookies_var = tk.IntVar()
# use_cookies_checkbox = tk.Checkbutton(window, text="Use Cookies", variable=use_cookies_var)
# use_cookies_checkbox.pack()
#
# # Custom User Agent
# user_agent_label = tk.Label(window, text="Custom User Agent:")
# user_agent_label.pack()
# user_agent_entry = ttk.Entry(window)
# user_agent_entry.pack()
#
# # Custom Headers
# headers_label = tk.Label(window, text="Custom Headers:")
# headers_label.pack()
# headers_entry = ttk.Entry(window)
# headers_entry.pack()
#
# # Run Scraper Button
# run_button = ttk.Button(window, text="Run Scraper", command=run_scraper)
# run_button.pack()
#
# # Start the UI event loop
# window.mainloop()
