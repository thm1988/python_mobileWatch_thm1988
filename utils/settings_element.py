from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

# DEFINE AUTO BRIGHTNESS LEVEL
# AUTO
_1_BRIGHTNESS_LEVEL = 60
_2_BRIGHTNESS_LEVEL = 90
_3_BRIGHTNESS_LEVEL = 120

# MANUAL
BRIGHTNESS_LEVEL_MANUAL = [50, 90, 140, 210, 250]

_display_element = "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Display\"))"

_connectivity_element = "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Connectivity\"))"
_connectivity_button = "//android.widget.Button[@text='Connectivity']"

_bluetooth_element = "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Bluetooth\"))"

_bluetooth_check_element = "com.google.android.apps.wearable.settings:id/wear_chip_selection_control"

_bluetooth_button = "//android.widget.Button[@text='Bluetooth']"

_display_button = "//android.widget.Button[@text='Display']"

_adjust_brightness_element = "new UiScrollable(new UiSelector()).scrollIntoView(text(""\"Adjust brightness\"))"

_adjust_brightness_button = "//android.widget.Button[@text='Adjust brightness']"

_adaptive_brightness_checked = "com.google.android.apps.wearable.settings:id/wear_chip_selection_control"

_adaptive_brightness_dec_ID = "//android.widget.ImageView[@content-desc=\"Decrease brightness\"]"

_adaptive_brightness_inc_ID = "//android.widget.ImageView[@content-desc=\"Increase brightness\"]"
