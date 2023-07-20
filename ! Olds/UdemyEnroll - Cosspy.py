import time
import numpy as np
import pyautogui
import pygetwindow as gw
import cv2
import csv


class UdemyEnroller:
    def __init__(self):
        # Path to image files
        self.freeImg = 'images/free.png'
        self.buynowImg = 'images/buynow.png'
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


    def check_course_free(self, link):
        if not self.find_image_on_screen(self.freeImg) and self.find_image_on_screen(self.buynowImg):
            print("Course is not free. Skipping to the next link.")
            pyautogui.hotkey('ctrl', 'w')  # Close the current tab
            with open('CouldNotEnroll.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([link])
            return False
        return True

    def click_enroll_button(self):
        if self.find_image_on_screen(self.Enroll1Img):
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

    def check_enrollment_success(self, link, enrolled_links):
        if self.find_image_on_screen(self.startcourseImg):
            print("Enrollment successful. Adding link to alreadyEnrolled.csv.")
            # Add the link to the list of enrolled links
            enrolled_links.append(link)
            self.appendToAlreadyEnrolled(link)
            return True
        return False

    def enroll_in_free_course(self,link):
        if self.find_image_on_screen(self.freeenroll):
            enroll_button = self.find_image_on_screen(self.freeenroll)
            pyautogui.moveTo(enroll_button)
            pyautogui.click()
            self.appendToAlreadyEnrolled(link)
            print("Enrolled in the Free Enroll Course.")


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

        # Create a file to store links where enrollment failed
        with open('CouldNotEnroll.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(link)

        # New list to store links that were successfully enrolled
        enrolled_links = []

        # Loop through each link
        for link in links:
            link = link[0]  # Extract the link from the list

            self.open_link_in_new_tab(link)

            # Check if the course is already enrolled
            if self.check_already_enrolled():
                self.appendToAlreadyEnrolled(link)
                continue

            # Check if the course is free
            if not self.check_course_free(link):
                continue

            # Find and click on 'Enroll Now' button
            self.click_enroll_button()

            # Check if enrollment was successful
            if self.check_enrollment_success(link, enrolled_links):
                pass
            else:
                self.enroll_in_free_course(link)

            self.close_current_tab()

        # Remove enrolled links from the original links list
        links = [link for link in links if link[0] not in enrolled_links]

        # Save the updated links to the 'courses_links.csv' file
        with open('courses_links.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(links)

        print("All links processed.")


enroller = UdemyEnroller()
enroller.enroll_courses('courses_links.csv')
