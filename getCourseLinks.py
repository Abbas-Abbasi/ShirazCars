import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, TimeoutException


class UdemyCourseScraper:
    def __init__(self, linkElementXPath, nextButtonXPath, getCouponBtnXPATH, website):
        self.driver = None
        self.wait = None
        self.linkElementXPath = linkElementXPath
        self.nextButtonXPath = nextButtonXPath
        self.getCouponBtnXPATH = getCouponBtnXPATH
        self.website = website

    def setup_driver(self):
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

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 50)

    def scrape_links_load_more(self, num_pages):
        try:
            self.driver.get(self.website)

            # Wait for the page to fully load
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.linkElementXPath)))

            if self.website == "https://www.real.discount/free-online-courses/":
                try:
                    load_more_btn = self.driver.find_element(By.XPATH, self.nextButtonXPath)
                    for _ in range(num_pages):
                        load_more_btn.click()
                        time.sleep(1)  # Sleep for 1 second
                except NoSuchElementException:
                    print("Next button not found. Skipping loading more pages.")

            # Wait for the page to fully load
            time.sleep(20)  # Sleep for 20 seconds
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.linkElementXPath)))

            links = self.driver.find_elements(By.XPATH, self.linkElementXPath)
            course_links = set()

            # Open each link in a new tab
            for link in links:
                link_url = link.get_attribute('href')

                if "real.discount/out-ad" in link_url or "real.discount/ads/saadmerie" in link_url:
                    continue

                self.driver.execute_script('window.open("' + link_url + '","_blank");')
                self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to the newly opened tab

                try:
                    # Wait for the page to fully load
                    self.wait.until(EC.presence_of_element_located((By.XPATH, self.getCouponBtnXPATH)))

                    # Get the link from getCouponBtnXPATH
                    coupon_btn = self.driver.find_element(By.XPATH, self.getCouponBtnXPATH)
                    course_link = coupon_btn.get_attribute('href')

                    course_links.add(course_link)

                    print(course_link)

                except NoSuchElementException:
                    print("Coupon button not found. Continuing to the next tab.")

                except TimeoutException:
                    print("Timeout occurred while waiting for the coupon button. Continuing to the next tab.")

                except NoSuchWindowException:
                    print("New tab not found. Continuing to the next tab.")

                self.driver.close()  # Close the current tab
                self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original tab

            self.save_links_to_csv(course_links)

        except NoSuchElementException:
            print("Elements not found on the page.")

    def scrape_links_next_page(self, num_pages):
        try:
            self.driver.get(self.website)

            course_links = set()

            for _ in range(num_pages):
                try:
                    # Wait for the page to fully load
                    self.wait.until(EC.presence_of_element_located((By.XPATH, self.linkElementXPath)))

                    links = self.driver.find_elements(By.XPATH, self.linkElementXPath)

                    # Open each link in a new tab
                    for link in links:
                        link_url = link.get_attribute('href')

                        if "real.discount/out-ad" in link_url or "real.discount/ads/saadmerie" in link_url:
                            continue

                        self.driver.execute_script('window.open("' + link_url + '","_blank");')
                        self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to the newly opened tab

                        # Wait for the page to fully load
                        time.sleep(3)

                        try:
                            # Wait for the getCouponBtnXPATH button to be visible
                            self.wait.until(EC.presence_of_element_located((By.XPATH, self.getCouponBtnXPATH)))

                            # Get the link from getCouponBtnXPATH
                            coupon_btn = self.driver.find_element(By.XPATH, self.getCouponBtnXPATH)
                            course_link = coupon_btn.get_attribute('href')

                            course_links.add(course_link)

                            print(course_link)

                        except NoSuchElementException:
                            print("Coupon button not found. Continuing to the next tab.")

                        except NoSuchWindowException:
                            print("New tab not found. Continuing to the next tab.")

                        self.driver.close()  # Close the current tab
                        self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original tab

                    try:
                        # Click the nextButtonXPath to navigate to the next page
                        next_button = self.driver.find_element(By.XPATH, self.nextButtonXPath)
                        next_button.click()
                    except NoSuchElementException:
                        print("Elements not found on the page.")

                except NoSuchElementException:
                    print("Elements not found on the page.")

            self.save_links_to_csv(course_links)

        except NoSuchElementException:
            print("Elements not found on the page.")

    def scrape_links_next_page_long_load(self, num_pages):
        try:
            self.driver.get(self.website)

            course_links = set()

            for _ in range(num_pages):
                try:
                    # Wait for the page to fully load
                    self.wait.until(EC.presence_of_element_located((By.XPATH, self.linkElementXPath)))

                    links = self.driver.find_elements(By.XPATH, self.linkElementXPath)

                    # Open each link in a new tab
                    for link in links:
                        link_url = link.get_attribute('href')

                        if "real.discount/out-ad" in link_url or "real.discount/ads/saadmerie" in link_url:
                            continue

                        self.driver.execute_script('window.open("' + link_url + '","_blank");')
                        self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to the newly opened tab

                        # Wait for the page to fully load (longer wait time for the coupon button)
                        time.sleep(25)

                        try:
                            # Wait for the getCouponBtnXPATH button to be visible
                            self.wait.until(EC.presence_of_element_located((By.XPATH, self.getCouponBtnXPATH)))

                            # Get the link from getCouponBtnXPATH
                            coupon_btn = self.driver.find_element(By.XPATH, self.getCouponBtnXPATH)
                            course_link = coupon_btn.get_attribute('href')

                            course_links.add(course_link)

                            print(course_link)

                        except NoSuchElementException:
                            print("Coupon button not found. Continuing to the next tab.")

                        except NoSuchWindowException:
                            print("New tab not found. Continuing to the next tab.")

                        self.driver.close()  # Close the current tab
                        self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original tab

                    try:
                        # Click the nextButtonXPath to navigate to the next page
                        next_button = self.driver.find_element(By.XPATH, self.nextButtonXPath)
                        next_button.click()
                    except NoSuchElementException:
                        print("Elements not found on the page.")

                except NoSuchElementException:
                    print("Elements not found on the page.")

            self.save_links_to_csv(course_links)

        except NoSuchElementException:
            print("Elements not found on the page.")

    def save_links_to_csv(self, links):
        # Check if new_courses_links.csv already exists and load links from it
        existing_links = set()
        if os.path.exists('new_courses_links.csv'):
            with open('new_courses_links.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                existing_links.update(row[0] for row in reader)

        # Append unique links to new_courses_links.csv
        with open('new_courses_links.csv', 'a', newline='', encoding='UTF8') as csvfile:
            writer = csv.writer(csvfile)
            for link in links:
                if link not in existing_links:
                    writer.writerow([link])
                    existing_links.add(link)

    def close_driver(self):
        self.driver.quit()


# #############################################################################
# # Example usage
# linkElementXPath = '//*[@id="myList"]/li/a'
# nextButtonXPath = '//*/div/div/div[2]/div[3]/input'
# getCouponBtnXPATH = '/html/body/div[2]/div/div[2]/div[3]/div/a'
# website = "https://www.real.discount/free-online-courses/"
#
# scraper1 = UdemyCourseScraper(linkElementXPath, nextButtonXPath, getCouponBtnXPATH, website)
# scraper1.setup_driver()
# scraper1.scrape_links_load_more(3)  # Scrape 3 pages
# scraper1.close_driver()
# #############################################################################
# # Example with different configurations
# linkElementXPath2 = '//*/article/div[1]/div/div/h3/a'
# nextButtonXPath2 = '/html/body/div[1]/div[2]/div/div/div/article/div/div[1]/div/ul/li[6]/a'
# getCouponBtnXPATH2 = '//*/div[4]/div[2]/div/span[2]/a'
# website2 = "https://couponscorpion.com/"
#
# scraper2 = UdemyCourseScraper(linkElementXPath2, nextButtonXPath2, getCouponBtnXPATH2, website2)
# scraper2.setup_driver()
# scraper2.scrape_links_next_page_long_load(2)  # Scrape 2 pages
# scraper2.close_driver()
# #############################################################################
# # Example with different configurations
# linkElementXPath3 = '//*[@id="coupon-page"]/div/div/div[1]/div/div/div/div[1]/h4/a'
# nextButtonXPath3 = '//*[@id="coupon-page"]/div/div/div[1]/ul/li[8]/a'
# getCouponBtnXPATH3 = '//*[@id="coupon-page"]/div/div/div[1]/div/div/div[3]/div/a'
# website3 = "https://udemyfreebies.com/"
#
# scraper3 = UdemyCourseScraper(linkElementXPath3, nextButtonXPath3, getCouponBtnXPATH3, website3)
# scraper3.setup_driver()
# scraper3.scrape_links_next_page(2)  # Scrape 2 pages
# scraper3.close_driver()
# #############################################################################
