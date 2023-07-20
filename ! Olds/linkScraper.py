from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

##################################################
linkElementXPath = '//*[@id="myList"]/li/a'
LoadMoreBTNXPath = '//*[@id="filters"]/div/div/div[2]/div[3]/input'

website = "https://www.real.discount/free-online-courses/"
driver = webdriver.Chrome()
driver.get(website)
##################################################
# Wait for the page to fully load
wait = WebDriverWait(driver, 100)
wait.until(EC.presence_of_element_located((By.XPATH, LoadMoreBTNXPath)))
##################################################
loadMoreBTN = driver.find_element(By.XPATH, LoadMoreBTNXPath)
loadMoreBTN.click()
time.sleep(1)  # Sleep for 1 seconds
loadMoreBTN.click()
time.sleep(1)  # Sleep for 1 seconds
loadMoreBTN.click()
time.sleep(1)  # Sleep for 1 seconds

##################################################
time.sleep(10)  # Sleep for 10 seconds
getCouponBtnXPATH = "/html/body/div[2]/div/div[2]/div[3]/div[2]/a"



wait.until(EC.presence_of_element_located((By.XPATH, linkElementXPath)))
links = driver.find_elements(By.XPATH, linkElementXPath)
open each element in links in a new tab
then wait for wait.until(EC.presence_of_element_located((By.XPATH, getCouponBtnXPATH))) then look for getCouponBtnXPATH and then get the links from getCouponBtnXPATH button
    and then save them in courseLinks as a list

# print(links)
##################################################

# Open the CSV file in write mode
with open('sitelinks.csv', 'w', newline='', encoding='UTF8') as csvfile:
    writer = csv.writer(csvfile)
    # Write each link as a row in the CSV file
    for link in courseLinks:
        siteLinks = link.get_attribute('href')
        if "real.discount/out-ad" not in siteLinks and "real.discount/ads/saadmerie" not in siteLinks:


            writer.writerow([siteLinks])
            print(siteLinks)
##################################################




##################################################
# driver.quit()
