import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Replace 'PROFILE_DIRECTORY_PATH' with the actual path of the Chrome profile directory
profile_directory = 'C:/Users/Trickster/AppData/Local/Google/Chrome/User Data/Profile1'
data_directory = 'C:/Users/Trickster/AppData/Local/Google/Chrome/User Data'

chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={data_directory}")
chrome_options.add_argument(f"--user-data-dir={profile_directory}")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def setup_driver():
    chrome_options = Options()

    # Enable JavaScript
    chrome_options.add_argument("--enable-javascript")

    # Start Chrome maximized
    chrome_options.add_argument("--start-maximized")

    # Set a custom user-agent (optional)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    chrome_options.add_argument(f"--user-agent={user_agent}")

    # Add other options if needed

    # Create the WebDriver with ChromeOptions
    driver = webdriver.Chrome(options=chrome_options)

    return driver


# Usage
driver = setup_driver()
driver.get("https://www.udemy.com")
time.sleep(100)
# Perform your browsing actions here

# Close the browser when done
# driver.quit()
