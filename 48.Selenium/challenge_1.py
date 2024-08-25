from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()  # or webdriver.Chrome(options=chrome_options)

event = []

try:

    # Open the website
    driver.get("https://www.python.org/")
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div[2]/div[2]/div/ul")

    list_el = element.text.split("\n")
    # print(list_el)

    # Skip every second element (step by 2)
    event_date = list_el[::2]
    # print(event_date)

    # Skip every second element (step by 2)
    event_name = list_el[1::2]
    # print(event_name)

    # Create in a nested dictionary

    # using loop method
    upcoming = {}
    for i in range(len(event_name)):
        upcoming[f"event_{i + 1}"] = {
            "name": event_name[i],
            "time": event_date[i]
        }
    print(upcoming)

#     Angela's solution(her code has put mine to shame)
    event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
    event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
    events = {}

    for n in range(5):
        events[n] = {
            "time": event_times[n].text,
            "name": event_names[n].text,
        }
    print(events)


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.close()
