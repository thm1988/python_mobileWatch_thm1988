import time

import pytest as pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def launchApp(host="http://localhost:4723/wd/hub", udid="K6S4001124B0049", **kwargs):
    desired_caps = {}
    desired_caps['udid'] = udid
    desired_caps['platformName'] = 'android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps.update(kwargs)
    return webdriver.Remote(host, desired_caps)


@pytest.fixture(scope="session")
def driver():
    driver = launchApp(noReset=True)
    return driver


def test_start_fossil_phone_app(driver):
    driver.start_activity("com.fossil.phone", "com.fossil.phone.dialer.DialerActivity")
    assert driver.current_activity in "com.fossil.phone.dialer.DialerActivity"


def test_start_message_app(driver):
    driver.start_activity("com.google.android.apps.messaging",
                          "com.google.android.apps.messaging.main.WearMainActivity")
    assert driver.current_activity in "com.google.android.apps.messaging.main.WearMainActivity"
    # driver.execute_script('mobile: longClickGesture', {'x': 250, 'y': 270, 'duration': 1000})
    # can_swipe = driver.execute_script('mobile: swipeGesture', {
    #     "left", 100, "top", 100, "width", 200, "height", 332,
    #     "direction", "up",
    #     "percent", 1
    # })
    # driver.find_element(AppiumBy.ID, "com.fossil.phone:id/tv_settings").click()

    time.sleep(10)
    driver.quit()
