import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the Chrome driver
driver = webdriver.Chrome()  # or webdriver.Chrome(options=chrome_options)

try:

    # Open the website
    driver.get("http://secure-retreat-92358.herokuapp.com/")

    fname = driver.find_element(By.NAME, "fName")
    fname.send_keys("Ugochukwu")

    lname = driver.find_element(By.NAME, "lName")
    lname.send_keys("George")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("pyth128@gmail.com")

    sign_up = driver.find_element(By.CSS_SELECTOR, "form button")
    sign_up.click()

    time.sleep(10)


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.close()
