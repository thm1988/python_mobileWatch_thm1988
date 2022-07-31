from appium.webdriver.common.appiumby import AppiumBy

touch_to_wake_elem = (AppiumBy.XPATH,"(//android.widget.Switch[@content-desc='Touch-to-wake'])[2]")
tilt_to_wake_elem = (AppiumBy.XPATH,"(//android.widget.Switch[@content-desc='Tilt-to-wake'])[2]")


class GesturesScreen:
    def is_TiltToWake_ON(driver):
        touch_to_wake_switch = driver.find_element(touch_to_wake_elem)
        return touch_to_wake_switch.get_attribute("checked") == 'true'

    def is_TouchToWake_ON(driver):
        touch_to_wake_switch = self.driver.find_element(tilt_to_wake_elem)
        return touch_to_wake_switch.get_attribute("checked") == 'true'
