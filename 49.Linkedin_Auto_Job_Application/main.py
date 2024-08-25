from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Retrieve email and password from environment variables
my_email = os.environ.get("LINKED_MY_EMAIL")
password = os.environ.get("LINKED_MY_PASSWORD")

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F"
           "%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_LF%3Df_AL%26geoId%3D102257491%26keywords%3Dpython"
           "%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom%26redirect%3Dfalse"
           "%26position%3D1%26pageNum%3D0&trk=public_jobs_nav-header-signin")

linkedin_login_0 = driver.find_element(By.ID, "username")
linkedin_login_0.send_keys(my_email)

linkedin_login_1 = driver.find_element(By.ID, "password")
linkedin_login_1.send_keys(password)

sign_up = driver.find_element(By.CSS_SELECTOR, "div button")
sign_up.click()


# current job
no = 0

# Get list of companies
company_list = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
item_ids = [item.get_attribute("id") for item in company_list]
print(item_ids)


def fill_form():
    time.sleep(2)
    easy_apply_button = driver.find_element(By.CSS_SELECTOR, ".mt5 button")
    easy_apply_button.click()

    time.sleep(2)
    phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
    if phone.text == "":
        phone.send_keys("000000000000")
    elif phone.text == "000000000000":
        pass

    time.sleep(2)
    next_button = driver.find_element(By.CSS_SELECTOR, "footer button")
    next_button.click()

    progress_bar = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div/div/progress")

    # Retrieve the current value of the progress bar
    progress_value = int(progress_bar.get_attribute("value"))
    print(f"Current value of the progress bar: {progress_value}%")
    if progress_value == 50:
        # NEXT LEVEL
        time.sleep(2)
        review_button = driver.find_element(By.XPATH,
                                            "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
        review_button.click()

        submit_button = driver.find_element(By.XPATH,
                                            "/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]")
        submit_button.click()

        no_thanks = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]")
        no_thanks.click()

        dismiss = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button/svg/use")
        dismiss.click()

    else:
        back_button = driver.find_element(By.XPATH,
                                          "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[1]")
        back_button.click()

        dismiss_button = driver.find_element(By.XPATH,
                                             "/html/body/div[3]/div/div/button")

        dismiss_button.click()

        discard_button = driver.find_element(By.XPATH,
                                             "/html/body/div[3]/div[2]/div/div[3]/button[1]")

        discard_button.click()


while True:
    # function to fill form
    fill_form()

    # working on the numbers
    num = len(item_ids)
    no += 1

    # Next Job
    job = driver.find_element(By.ID, item_ids[no])
    job.click()

    if no == num:
        break
    else:
        continue
driver.close()
