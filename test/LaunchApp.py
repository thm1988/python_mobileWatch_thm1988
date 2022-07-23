import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

APPIUM = 'http://127.0.0.1:4723/wd/hub'
CAPS = {
    'platformName': 'Android',
    'udid': 'K6F1081454B3395',
    'automationName': 'UiAutomator2',
    'appPackage': 'com.nike.plusgps',
    'appActivity': 'com.nike.plusgps.activities.MainActivity',
}
driver = webdriver.Remote(APPIUM, CAPS)
timeout = 5
try:
    element_present = EC.presence_of_element_located((By.ID, 'com.nike.plusgps:id/login_text'))
    WebDriverWait(driver, timeout).until(element_present)
    el = driver.find_element(AppiumBy.ID, 'com.nike.plusgps:id/login_text')
    el.click()
    WebDriverWait(driver, timeout)
except TimeoutException:
    print("Timed out waiting for screen to load")
driver.quit()


