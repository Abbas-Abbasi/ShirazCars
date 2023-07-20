from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
from selenium.common.exceptions import NoSuchElementException


class UdemyCourseScraper:
    def __init__(self, linkElementXPath, nextButtonXPath, getCouponBtnXPATH, website):
        self.driver = None
        self.wait = None
        self.linkElementXPath = linkElementXPath
        self.nextButtonXPath = nextButtonXPath
        self.getCouponBtnXPATH = getCouponBtnXPATH
        self.website = website

    def setup_driver(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 100)

    def scrape_links_load_more(self):
        self.driver.get(self.website)

        # Wait for the page to fully load
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.linkElementXPath)))

        if self.website == "https://www.real.discount/free-online-courses/":
            load_more_btn = self.driver.find_element(By.XPATH, self.nextButtonXPath)
            for _ in range(0):
                load_more_btn.click()
                time.sleep(1)  # Sleep for 1 second

        # Wait for the page to fully load
        time.sleep(10)  # Sleep for 10 seconds
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

            except:
                print("Error occurred. Continuing to the next tab.")

            self.driver.close()  # Close the current tab
            self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original tab

        # Open the CSV file in write mode
        with open('courses_links.csv', 'w', newline='', encoding='UTF8') as csvfile:
            writer = csv.writer(csvfile)
            # Write each link as a row in the CSV file
            writer.writerows([[link] for link in course_links])
            print(f"Total unique links: {len(course_links)}")

    def scrape_links_next_page(self, num_pages):
        self.driver.get(self.website)

        course_links = set()

        for _ in range(num_pages):
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
                time.sleep(30)

                try:
                    # Wait for the getCouponBtnXPATH button to be visible
                    self.wait.until(EC.presence_of_element_located((By.XPATH, self.getCouponBtnXPATH)))

                    # Get the link from getCouponBtnXPATH
                    coupon_btn = self.driver.find_element(By.XPATH, self.getCouponBtnXPATH)
                    course_link = coupon_btn.get_attribute('href')

                    course_links.add(course_link)

                    print(course_link)

                except NoSuchElementException:
                    print("Error occurred. Continuing to the next tab.")

                self.driver.close()  # Close the current tab
                self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original tab

            # Click the nextButtonXPath to navigate to the next page
            next_button = self.driver.find_element(By.XPATH, self.nextButtonXPath)
            next_button.click()

        # Open the CSV file in append mode
        with open('courses_links.csv', 'a', newline='', encoding='UTF8') as csvfile:
            writer = csv.writer(csvfile)
            # Write each link as a row in the CSV file
            writer.writerows([[link] for link in course_links])
            print(f"Total unique links: {len(course_links)}")

    def close_driver(self):
        self.driver.quit()


#############################################################################
#############################################################################
# Example usage
linkElementXPath = '//*[@id="myList"]/li/a'
nextButtonXPath = '//*[@id="filters"]/div/div/div[2]/div[3]/input'
getCouponBtnXPATH = '/html/body/div[2]/div/div[2]/div[3]/div[2]/a'
website = "https://www.real.discount/free-online-courses/"

scraper1 = UdemyCourseScraper(linkElementXPath, nextButtonXPath, getCouponBtnXPATH, website)
scraper1.setup_driver()
scraper1.scrape_links_load_more()
scraper1.close_driver()

#############################################################################
# Example with different configurations
linkElementXPath2 = '//*/article/div[1]/div/div/h3/a'
nextButtonXPath2 = '/html/body/div[1]/div[2]/div/div/div/article/div/div[1]/div/ul/li[6]/a'
getCouponBtnXPATH2 = '//*/div[4]/div[2]/div/span[2]/a'
website2 = "https://couponscorpion.com/"

scraper2 = UdemyCourseScraper(linkElementXPath2, nextButtonXPath2, getCouponBtnXPATH2, website2)
scraper2.setup_driver()
scraper2.scrape_links_next_page(2)  # Scrape 3 pages
scraper2.close_driver()


#############################################################################
# Example with different configurations
linkElementXPath3 = '//*[@id="coupon-page"]/div/div/div[1]/div/div/div/div[1]/h4/a'
nextButtonXPath3 = '//*[@id="coupon-page"]/div/div/div[1]/ul/li[8]/a'
getCouponBtnXPATH3 = '//*[@id="coupon-page"]/div/div/div[1]/div/div/div[3]/div/a'
website3 = "https://udemyfreebies.com/"

scraper3 = UdemyCourseScraper(linkElementXPath3, nextButtonXPath3, getCouponBtnXPATH3, website3)
scraper3.setup_driver()
scraper3.scrape_links_next_page(2)  # Scrape 3 pages
scraper3.close_driver()


#############################################################################
