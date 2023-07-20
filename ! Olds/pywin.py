import time
import pyautogui
import pygetwindow as gw
import cv2
import csv
import os

# Path to image files
freeImg = 'images/free.png'
Enroll1Img = 'images/EnrollNow1.png'
Enroll2Img = 'images/EnrollNow2.png'
startcourseImg = 'images/startcourse.png'
gotitIimg = 'images/gotit.png'
gotocourseImg = 'images/gotocourse.png'


# Function to perform template matching using OpenCV
def find_image_on_screen(template_path):
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    screenshot = pyautogui.screenshot()
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    threshold = 0.8  # You can adjust this threshold based on your needs
    if max_val >= threshold:
        return max_loc
    return None


# Wait for the user to focus on the Chrome window
time.sleep(5)

# Get the reference to the Chrome window
chrome_window = gw.getWindowsWithTitle("Google Chrome")[0]

# Activate the Chrome window (bring it to the front)
chrome_window.activate()

# Load the links from the CSV file
with open('courses_links.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    links = list(reader)

# Loop through each link
for link in links:
    link = link[0]  # Extract the link from the list

    # Open the link in Chrome
    pyautogui.hotkey('ctrl', 't')  # Open a new tab
    pyautogui.typewrite(link)  # Type the link into the address bar
    pyautogui.press('enter')  # Press Enter to navigate to the link

    # Wait for the page to load
    time.sleep(20)

    # Check if the course is already enrolled
    if find_image_on_screen(gotitIimg):
        print("Course already enrolled. Skipping to the next link.")
        pyautogui.hotkey('ctrl', 'w')  # Close the current tab
        continue

    # Find and click on 'Enroll Now' button
    if find_image_on_screen(freeImg) and find_image_on_screen(Enroll1Img):
        enroll_button = find_image_on_screen(Enroll1Img)
        pyautogui.moveTo(enroll_button)
        pyautogui.click()
        time.sleep(20)

        # Check if enrollment was successful
        if find_image_on_screen(Enroll2Img):
            print("Enrollment successful. Adding link to alreadyEnrolled.csv.")
            # Save the link to the 'alreadyEnrolled.csv' file
            if not os.path.exists('alreadyEnrolled.csv'):
                with open('alreadyEnrolled.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['Course Link'])
            with open('alreadyEnrolled.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([link])
        else:
            print("Enrollment unsuccessful. Link:", link)

    # Check if the course is already enrolled using alternative images
    elif find_image_on_screen(gotocourseImg) and find_image_on_screen(gotitIimg):
        print("Course already enrolled. Skipping to the next link.")

    else:
        print("Target text not found.")

    # Close the current tab
    pyautogui.hotkey('ctrl', 'w')

print("All links processed.")
