import time

import pytest as pytest
from appium import webdriver


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


def test_start_setting_app(driver):

    driver.start_activity("com.google.android.apps.wearable.settings",
                          "com.google.android.clockwork.settings.MainSettingsActivity")
    assert driver.current_activity in "com.google.android.clockwork.settings.MainSettingsActivity"

    time.sleep(10)
    driver.quit()
