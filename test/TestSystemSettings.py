import time

import pytest as pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy

from utils import helpers, settings_element
from screen.setting_screen import SettingScreen
from screen.gestures_screen import GesturesScreen


class TestSystemSettings:
    serial_number = "K6S4001124B0049"

    def launchApp(self, host="http://localhost:4723/wd/hub", udid=serial_number, **kwargs):
        self.desired_caps = {}
        self.desired_caps['udid'] = udid
        self.desired_caps['platformName'] = 'android'
        self.desired_caps['automationName'] = 'UiAutomator2'
        self.desired_caps.update(kwargs)
        return webdriver.Remote(host, self.desired_caps)

    @pytest.fixture(scope="function")
    def driver(self):
        self.driver = self.launchApp(appPackage="com.google.android.apps.wearable.settings",
                                     appActivity="com.google.android.clockwork.settings.MainSettingsActivity")
        yield self.driver

    def test_touch_to_wake_default_setting_should_be_ON_(self, driver):
        SettingScreen.navigateToScreen(self.driver, "Gestures")
        assert GesturesScreen.is_TiltToWake_ON(self.driver)

    def test_tilt_to_wake_default_setting_should_be_OFF_(self, driver):
        SettingScreen.navigateToScreen(self.driver, "Gestures")
        assert GesturesScreen.is_TouchToWake_ON(self.driver)

    # def test_adjust_brightness(self, driver):
    #     _1_brightness = int(helpers.get_screen_brightness())
    #     # Scroll to Display
    #     self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    #                              settings_element._display_element)
    #     # Tap on Display
    #     self.driver.find_element(AppiumBy.XPATH, settings_element._display_button).click()
    #
    #     # Scroll to Adjust brightness
    #     self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, settings_element._adjust_brightness_element)
    #
    #     # Click on the element
    #     self.driver.find_element(AppiumBy.XPATH, settings_element._adjust_brightness_button).click()
    #
    #     time.sleep(2)
    #
    #     # Case Adaptive brightness = ON
    #     _adaptive_brightness_check_el = self.driver.find_element(AppiumBy.ID, settings_element.
    #                                                              _adaptive_brightness_checked)
    #
    #     _adaptive_brightness_decrease_el = self.driver.find_element(AppiumBy.XPATH, settings_element
    #                                                                 ._adaptive_brightness_dec_ID)
    #
    #     _adaptive_brightness_increase_el = self.driver.find_element(AppiumBy.XPATH, settings_element
    #                                                                 ._adaptive_brightness_inc_ID)
    #
    #     if _adaptive_brightness_check_el.get_attribute("checked") == 'true':
    #         time.sleep(2)
    #         # Click on Decrease - 1st
    #         _adaptive_brightness_decrease_el.click()
    #
    #         time.sleep(2)
    #         # Click on Decrease - 2nd
    #         _adaptive_brightness_decrease_el.click()
    #
    #         assert _1_brightness < settings_element._1_BRIGHTNESS_LEVEL
    #
    #         # Click on Increase - 1st
    #         _adaptive_brightness_increase_el.click()
    #         _2_brightness = int(helpers.get_screen_brightness())
    #         assert _2_brightness < settings_element._2_BRIGHTNESS_LEVEL
    #
    #         # Click on Increase - 2nd
    #         _adaptive_brightness_increase_el.click()
    #         _3_brightness = int(helpers.get_screen_brightness())
    #         assert _3_brightness < settings_element._3_BRIGHTNESS_LEVEL
    #
    #     else:
    #         # Decrease brightness to level 1
    #         current_ind_dec = 0
    #         while current_ind_dec <= 4:
    #             _adaptive_brightness_decrease_el.click()
    #             current_ind_dec += 1
    #
    #         # Increase brightness from level 1 to level 5, step by step
    #         assert int(helpers.get_screen_brightness()) < settings_element.BRIGHTNESS_LEVEL_MANUAL[0]
    #         current_ind_inc = 1
    #         while current_ind_inc < 5:
    #             _adaptive_brightness_increase_el.click()
    #             assert int(helpers.get_screen_brightness()) < settings_element.BRIGHTNESS_LEVEL_MANUAL[current_ind_inc]
    #             current_ind_inc += 1
    #
    # def test_bluetooth_on_off_(self, driver):
    #     self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    #                              settings_element._connectivity_element)
    #     # Click on Connectivity button
    #     self.driver.find_element(AppiumBy.XPATH, settings_element._connectivity_button).click()
    #     self.driver.find_element(AppiumBy.XPATH, settings_element._bluetooth_button).click()
    #     time.sleep(2)
    #
    #     # Scroll to bluetooth element
    #     self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    #                              settings_element._bluetooth_element)
    #
    #     bluetooth_elem = self.driver.find_element(AppiumBy.XPATH,
    #                                               settings_element._bluetooth_button)
    #
    #     if bluetooth_elem.get_attribute("checked") == 'true':
    #         bluetooth_elem.click()
    #         assert bluetooth_elem.get_attribute("checked") == 'false'
    #         bluetooth_elem.click()
    #         assert bluetooth_elem.get_attribute("checked") == 'true'
    #     else:
    #         bluetooth_elem.click()
    #         assert bluetooth_elem.get_attribute("checked") == 'true'
    #         bluetooth_elem.click()
    #         assert bluetooth_elem.get_attribute("checked") == 'false'
