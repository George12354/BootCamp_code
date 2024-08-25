from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the Chrome driver
driver = webdriver.Chrome()  # or webdriver.Chrome(options=chrome_options)

try:

    # Open the website
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    element = driver.find_element(By.XPATH,
                                  "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]")
    print(element.text)
    # element.click()

    # how to find by link text name
    # all_portals = driver.find_element(By.LINK_TEXT, "Community portal")
    # all_portals.click()

    # how to find by the name
    search = driver.find_element(By.NAME, "search")

    search.send_keys("Python")
    search.send_keys(Keys.ENTER)


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.close()
