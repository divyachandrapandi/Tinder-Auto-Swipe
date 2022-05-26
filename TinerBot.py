from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

# -----------------------------CREDENTIALS-------------------------------#
EMAIL = "divya4shivalaya@gmail.com"
PASS_KEY = "Ganesh55*"

# -----------------------------URL-------------------------------#
TINDER_URL = "https://tinder.com/"

# -----------------------------SELENIUM SETUP-------------------------------#
chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

# -----------------------------GET HOME PAGE-------------------------------#
driver.get(TINDER_URL)
time.sleep(10)
login_button = driver.find_element(By.XPATH,
                                   '//*[@id="o285386697"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
time.sleep(5)
base_window = driver.window_handles[0]


# ----------------------------LOGIN PAGE------------------------------------#
try:
    if driver.find_element(By.XPATH, '//*[@id="o-1442994379"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').is_displayed():

        login_with_facebook = driver.find_element(By.XPATH,
                                                  '//*[@id="o-1442994379"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
        login_with_facebook.click()
        time.sleep(10)


except NoSuchElementException:
    more_options = driver.find_element(By.XPATH,
                                       '//*[@id="o-1442994379"]/div/div/div[1]/div/div/div[3]/span/button')
    more_options.click()
    time.sleep(5)

    login_with_facebook = driver.find_element(By.XPATH,
                                                  '//*[@id="o-1442994379"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
    login_with_facebook.click()
    time.sleep(5)

# ------------------------------FACEBOOK PAGE -------------------------#
finally:
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    print(driver.title)
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys(EMAIL)
    password_input = driver.find_element(By.ID, 'pass')
    password_input.send_keys(PASS_KEY)
    submit_button = driver.find_element(By.ID, "loginbutton" )
    submit_button.send_keys(Keys.ENTER)
    time.sleep(5)
# -----------------------------REVERT TO TENDER PAGE---------------------#
    driver.switch_to.window(base_window)
    print(driver.title)
    time.sleep(10)

    # -------------------------------DISMISS ALL REQUESTS------------------------------#
    allow_location = driver.find_element(By.XPATH, '//*[@id="o-1442994379"]/div/div/div/div/div[3]/button[1]')
    allow_location.click()
    policy_accept = driver.find_element(By.XPATH, '//*[@id="o285386697"]/div/div[2]/div/div/div[1]/div[1]/button')
    policy_accept.click()
    deny_notification = driver.find_element(By.XPATH, '//*[@id="o-1442994379"]/div/div/div/div/div[3]/button[2]')
    deny_notification.click()

# ------------------------------------DISLIKE - 100 [100 TIMES DAILY - FREE VERSION] ---------------#
time.sleep(20)
i = 0
while i< 5:
    try:
        if driver.find_element(By.XPATH, '//*[@id="o285386697"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button').is_displayed():
            dislike_button =driver.find_element(By.XPATH, '//*[@id="o285386697"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
            dislike_button.click()
            time.sleep(8)
    except NoSuchElementException:
        time.sleep(16)
        dislike_button = driver.find_element(By.XPATH,'//*[@id="o285386697"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
        dislike_button.click()
        time.sleep(8)

    except ElementClickInterceptedException:
        break
