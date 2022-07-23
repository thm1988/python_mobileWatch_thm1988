import time

import pytest as pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


def launchApp(host="http://localhost:4723/wd/hub", udid="K6F1021084B0061", **kwargs):
    desired_caps = {}
    desired_caps['udid'] = udid
    desired_caps['platformName'] = 'android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps.update(kwargs)
    return webdriver.Remote(host, desired_caps)


@pytest.fixture(scope="function")
def driver():
    driver = launchApp(appPackage="com.google.android.apps.wearable.settings",
                       appActivity="com.google.android.clockwork.settings.MainSettingsActivity")
    yield driver


def test_touch_to_wake_default_setting_should_be_ON_(driver):
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Gestures\"))")
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Gestures']").click()
    time.sleep(2)
    touch_to_wake_switch = driver.find_element(AppiumBy.XPATH,
                                               "(//android.widget.Switch[@content-desc='Touch-to-wake'])[2]")
    assert touch_to_wake_switch.get_attribute("checked") == 'true'


def test_tilt_to_wake_default_setting_should_be_OFF_(driver):
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Gestures\"))")
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Gestures']").click()
    time.sleep(2)
    touch_to_wake_switch = driver.find_element(AppiumBy.XPATH,
                                               "(//android.widget.Switch[@content-desc='Tilt-to-wake'])[2]")
    assert touch_to_wake_switch.get_attribute("checked") == 'false'


def test_adjust_brightness(driver):
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Display\"))")
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Display']").click()

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Adjust Brightness\"))")
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Adjust Brightness']").click()
