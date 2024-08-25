import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()

store = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime "
                                                                                                           "machine",
         "buyElder Pledge"]

# Open the website
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_clicker = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")
money_fig = int(money.text)
cookie_sec = driver.find_element(By.ID, "cps")


def cookie():
    # Need to loop this place

    if money_fig > 500:
        for item in store:
            store_item = driver.find_element(By.ID, f"{item}")
            store_item.click()


# Get the current time
start_time = time.time()
# Duration in seconds (5 minutes)
duration = 5 * 60

while True:
    cookie_clicker.click()
    # look for how to put time here, for every 5 seconds run code to check item to buy
    # time.sleep(5)
    cookie()

    # Check if 5 minutes have passed
    elapsed_time = time.time() - start_time
    if elapsed_time > duration:
        break

# Now print the "cookies/second"
print(cookie_sec.text)

# Close the browser
driver.close()
