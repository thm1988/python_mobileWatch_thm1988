import time
from appium.webdriver.common.appiumby import AppiumBy


class SettingScreen:
    def navigateToScreen(driver, name):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiScrollable(new UiSelector()).scrollIntoView(text(\"%s\"))" % name)
        driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='%s']" % name).click()
        time.sleep(2)
