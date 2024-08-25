from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.python.org/")

# Get element with id
element = driver.find_element(By.ID, "fruits")
print(element.text)

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, "//*[@id="container"]/li[3]/ul/li[5]/a")
# print(bug_link.text)

driver.close()
