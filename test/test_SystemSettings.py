import time

import pytest as pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy

from utils import helpers
from screen.setting_screen import SettingScreen
from screen.gestures_screen import GesturesScreen


def launchApp(self,host="http://localhost:4723/wd/hub", udid="K6S4001124B0049", **kwargs):
    self.desired_caps = {}
    self.desired_caps['udid'] = udid
    self.desired_caps['platformName'] = 'android'
    self.desired_caps['automationName'] = 'UiAutomator2'
    self.desired_caps.update(kwargs)
    return webdriver.Remote(host, self.desired_caps)

@pytest.fixture(scope="session")
def driver(self):
    self.driver = self.launchApp(appPackage="com.google.android.apps.wearable.settings",
                                appActivity="com.google.android.clockwork.settings.MainSettingsActivity")
    yield self.driver


def test_touch_to_wake_default_setting_should_be_ON(self, driver):
    SettingScreen.navigateToScreen(self.driver, "Gestures")
    assert GesturesScreen.is_TiltToWake_ON(self.driver)

def test_tilt_to_wake_default_setting_should_be_OFF(self, driver):
    SettingScreen.navigateToScreen(self.driver, "Gestures")
    assert GesturesScreen.is_TouchToWake_ON(self.driver)