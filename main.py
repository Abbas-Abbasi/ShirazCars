import csv
import os
from getCourseLinks import UdemyCourseScraper
from UdemyEnroll import UdemyCourseEnroll

def extract_unique_links():
    # Load existing enrolled links from alreadyEnrolled.csv
    existing_enrolled_links = set()
    if os.path.exists('alreadyEnrolled.csv'):
        with open('alreadyEnrolled.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            existing_enrolled_links.update(row[0] for row in reader)

    # Load new links from new_courses_links.csv
    new_links = set()
    if os.path.exists('new_courses_links.csv'):
        with open('new_courses_links.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            new_links.update(row[0] for row in reader)

    # Extract unique links by removing the links that are already enrolled
    unique_links = new_links - existing_enrolled_links

    # Save the unique links to courses_links.csv
    with open('courses_links.csv', 'w', newline='', encoding='UTF8') as csvfile:
        writer = csv.writer(csvfile)
        for link in unique_links:
            writer.writerow([link])

def main():
    # Step 1: Enroll in the courses using UdemyEnroller
    enroller = UdemyCourseEnroll()
    enroller.enroll_courses('courses_links.csv')

    # Step 2: Scrape for course Links
    #############################################################################
    # Example usage
    linkElementXPath = '//*[@id="myList"]/li/a'
    nextButtonXPath = '//*/div/div/div[2]/div[3]/input'
    getCouponBtnXPATH = '/html/body/div[2]/div/div[2]/div[3]/div/a'
    website = "https://www.real.discount/free-online-courses/"

    scraper1 = UdemyCourseScraper(linkElementXPath, nextButtonXPath, getCouponBtnXPATH, website)
    scraper1.setup_driver()
    scraper1.scrape_links_load_more(3)  # Scrape 3 pages
    scraper1.close_driver()
    #############################################################################
    # Example with different configurations
    linkElementXPath2 = '//*/article/div[1]/div/div/h3/a'
    nextButtonXPath2 = '/html/body/div[1]/div[2]/div/div/div/article/div/div[1]/div/ul/li[6]/a'
    getCouponBtnXPATH2 = '//*/div[4]/div[2]/div/span[2]/a'
    website2 = "https://couponscorpion.com/"

    scraper2 = UdemyCourseScraper(linkElementXPath2, nextButtonXPath2, getCouponBtnXPATH2, website2)
    scraper2.setup_driver()
    scraper2.scrape_links_next_page_long_load(2)  # Scrape 2 pages
    scraper2.close_driver()
    #############################################################################
    # Example with different configurations
    linkElementXPath3 = '//*[@id="coupon-page"]/div/div/div[1]/div/div/div/div[1]/h4/a'
    nextButtonXPath3 = '//*[@id="coupon-page"]/div/div/div[1]/ul/li[8]/a'
    getCouponBtnXPATH3 = '//*[@id="coupon-page"]/div/div/div[1]/div/div/div[3]/div/a'
    website3 = "https://udemyfreebies.com/"

    scraper3 = UdemyCourseScraper(linkElementXPath3, nextButtonXPath3, getCouponBtnXPATH3, website3)
    scraper3.setup_driver()
    scraper3.scrape_links_next_page(2)  # Scrape 2 pages
    scraper3.close_driver()
    #############################################################################


    # Step 3: Extract unique links and save them to courses_links.csv
    extract_unique_links()

if __name__ == "__main__":
    main()
