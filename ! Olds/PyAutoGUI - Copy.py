import time
import pyautogui
import pygetwindow as gw
import cv2
import numpy as np

# Wait for the user to focus on the Chrome window
time.sleep(5)

# Get the reference to the Chrome window
chrome_window = gw.getWindowsWithTitle("Google Chrome")[0]

# Activate the Chrome window (bring it to the front)
chrome_window.activate()

# Open the link in Chrome
# link = "https://www.udemy.com/course/fast-bootstrap-by-3-live-responsive-websites-in-bootstrap-5/?couponCode=JULY_FREE_31"
# pyautogui.hotkey('ctrl', 't')  # Open a new tab
# pyautogui.typewrite(link)     # Type the link into the address bar
# pyautogui.press('enter')      # Press Enter to navigate to the link

# Wait for the page to load (you might need to adjust the sleep time)
time.sleep(20)

# Load the target image using OpenCV
target_image_path = 'images/gotocourse.png'
target_image = cv2.imread(target_image_path)

# Convert the target image to grayscale
target_gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

# Use template matching to find the location of the target image on the screen
screenshot = pyautogui.screenshot()
screenshot = np.array(screenshot)
screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
result = cv2.matchTemplate(screenshot_gray, target_gray, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
h, w = target_gray.shape

# The threshold value here (0.8) can be adjusted based on your needs
threshold = 0.8
if max_val >= threshold:
    bottom_right = (top_left[0] + w, top_left[1] + h)
    center_x = top_left[0] + w // 2
    center_y = top_left[1] + h // 2

    # Move the mouse to the center of the located image and click
    pyautogui.moveTo(center_x, center_y, duration=0.5)
    pyautogui.click()
else:
    print("Target text not found.")
