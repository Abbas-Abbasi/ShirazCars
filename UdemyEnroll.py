import time
import numpy as np
import pyautogui
import pygetwindow as gw
import cv2
import csv


class UdemyCourseEnroll:
    def __init__(self):
        # Path to image files
        self.freeImg = 'images/free.png'
        self.buynowImg = 'images/buynow.png'
        self.buynow2Img = 'images/buynow2.png'
        self.completecheckoutImg = 'images/completecheckout.png'
        self.Enroll1Img = 'images/EnrollNow1.png'
        self.Enroll2Img = 'images/EnrollNow2.png'
        self.startcourseImg = 'images/startcourse.png'
        self.gotitIimg = 'images/gotit.png'
        self.gotocourseImg = 'images/gotocourse.png'
        self.freeenroll = 'images/freeenroll.png'
        self.freegoto = 'images/freegoto.png'

    def find_image_on_screen(self, template_path, max_wait=10):
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        start_time = time.time()

        while time.time() - start_time <= max_wait:
            screenshot = pyautogui.screenshot()
            screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
            result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            threshold = 0.8  # You can adjust this threshold based on your needs
            if max_val >= threshold:
                return max_loc
            time.sleep(1)  # Sleep for 1 second and try again
        return None

    def open_link_in_new_tab(self, link):
        pyautogui.hotkey('ctrl', 't')  # Open a new tab
        pyautogui.typewrite(link)  # Type the link into the address bar
        pyautogui.press('enter')  # Press Enter to navigate to the link
        time.sleep(3)  # Wait for the page to load

    def append_to_already_enrolled(self, link):
        # Append to the file to store links where enrollment is successful
        with open('alreadyEnrolled.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([link[0]])  # Use link[0] to extract the link from the list


    def could_not_enroll_links(self, link):
        # Append to the file to store links where enrollment failed
        with open('CouldNotEnroll.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([link])

    def check_already_enrolled(self, link):
        if self.find_image_on_screen(self.gotitIimg) or self.find_image_on_screen(self.freegoto):
            print("Course already enrolled. Skipping to the next link.")
            pyautogui.hotkey('ctrl', 'w')  # Close the current tab
            return True
        return False

    def check_course_free(self, link):
        if not self.find_image_on_screen(self.freeImg) and self.find_image_on_screen(self.buynowImg):
            print("Course is not free. Skipping to the next link.")
            pyautogui.hotkey('ctrl', 'w')  # Close the current tab
            self.could_not_enroll_links(link)
            return False
        return True

    def enroll_coupon_course(self, link):
        if self.find_image_on_screen(self.Enroll1Img) and self.find_image_on_screen(self.freeImg):
            enroll_button = self.find_image_on_screen(self.Enroll1Img)
            pyautogui.moveTo(enroll_button)
            pyautogui.click()
            print("Clicked on the First Enroll Button.")
            time.sleep(3)

        if self.find_image_on_screen(self.Enroll2Img):
            enroll_button = self.find_image_on_screen(self.Enroll2Img)
            pyautogui.moveTo(enroll_button)
            time.sleep(3)
            pyautogui.click()
            print("Clicked on the Second Enroll Button.")
            time.sleep(3)

        if self.find_image_on_screen(self.startcourseImg):
            print("Enrollment successful. Adding link to alreadyEnrolled.csv.")
            # Add the link to the list of enrolled links
            self.append_to_already_enrolled(link)

    def enroll_checkout_course(self, link):
        if self.find_image_on_screen(self.freeImg) and self.find_image_on_screen(self.buynowImg):
            enroll_button = self.find_image_on_screen(self.buynowImg)
            pyautogui.moveTo(enroll_button)
            pyautogui.click()
            print("Clicked on the First Buy now Button.")
            time.sleep(3)

        if self.find_image_on_screen(self.buynow2Img):
            enroll_button = self.find_image_on_screen(self.buynow2Img)
            pyautogui.moveTo(enroll_button)
            time.sleep(3)
            pyautogui.click()
            print("Clicked on the Second Buy now Button.")
            time.sleep(3)

        if self.find_image_on_screen(self.completecheckoutImg):
            enroll_button = self.find_image_on_screen(self.completecheckoutImg)
            pyautogui.moveTo(enroll_button)
            time.sleep(3)
            pyautogui.click()
            print("Clicked on the Second Complete Checkout Button.")
            time.sleep(3)

        if self.find_image_on_screen(self.Enroll2Img):
            enroll_button = self.find_image_on_screen(self.Enroll2Img)
            pyautogui.moveTo(enroll_button)
            time.sleep(3)
            pyautogui.click()
            print("Clicked on the Second Enroll Button.")
            time.sleep(3)

        if self.find_image_on_screen(self.startcourseImg):
            print("Enrollment successful. Adding link to alreadyEnrolled.csv.")
            # Add the link to the list of enrolled links
            self.append_to_already_enrolled(link)

    def enroll_in_free_course(self, link):
        if self.find_image_on_screen(self.freeenroll):
            enroll_button = self.find_image_on_screen(self.freeenroll)
            pyautogui.moveTo(enroll_button)
            pyautogui.click()
            self.append_to_already_enrolled(link)
            print("Enrolled in the Free Enroll Course.")
            time.sleep(1)

    def close_current_tab(self):
        pyautogui.hotkey('ctrl', 'w')

    def enroll_courses(self, links_file):
        # Wait for the user to focus on the Chrome window
        time.sleep(10)

        # Get the reference to the Chrome window
        chrome_window = gw.getWindowsWithTitle("Google Chrome")[0]

        # Activate the Chrome window (bring it to the front)
        chrome_window.activate()

        # Load the links from the CSV file
        with open(links_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            links = list(reader)

        # New list to store links that were successfully enrolled
        enrolled_links = []

        for link in links:
            link = link[0]  # Extract the link from the list

            self.open_link_in_new_tab(link)

            # Check if the course is already enrolled
            if self.check_already_enrolled(link):
                continue

            # Check if the course is free and which type of enrollment to perform
            if not self.check_course_free(link):
                continue

            if self.find_image_on_screen(self.Enroll1Img) and self.find_image_on_screen(self.freeImg):
                self.enroll_coupon_course(link)
            elif self.find_image_on_screen(self.freeImg) and self.find_image_on_screen(self.buynowImg):
                self.enroll_checkout_course(link)
            elif self.find_image_on_screen(self.freeenroll):
                self.enroll_in_free_course(link)

            # Add successfully enrolled links to the list
            if self.find_image_on_screen(self.startcourseImg):
                enrolled_links.append(link)

            self.close_current_tab()

        # Append enrolled links to the 'alreadyEnrolled.csv' file
        for link in enrolled_links:
            self.append_to_already_enrolled(link)

        # Remove enrolled links from the original links list
        links = [link for link in links if link[0] not in enrolled_links]

        # Save the updated links to the 'courses_links.csv' file
        with open('courses_links.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(links)

        print("All links processed.")





enroller = UdemyCourseEnroll()
enroller.enroll_courses('courses_links.csv')
