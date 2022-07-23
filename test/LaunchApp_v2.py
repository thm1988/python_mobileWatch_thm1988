import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def launchApp(host="http://localhost:4723/wd/hub", udid="K6F1021084B0061", **kwargs):
    desired_caps = {'udid': udid, 'platformName': 'android', 'automationName': 'UiAutomator2'}
    desired_caps.update(kwargs)
    return webdriver.Remote(host, desired_caps)


if __name__ == '__main__':
    # driver = launchApp(
    #    app="/Users/pthanh2/Documents/AUTOMATION/0_HADO_FOSSIL/0_CODE/pythonThuPhamMobile/app/com.nike.plusgps.apk",
    #    appPackage="com.nike.plusgps", appActivity="com.nike.plusgps.activities.MainActivity")
    driver = launchApp(
        appPackage = "com.fossil.phone", appActivity = "com.fossil.phone.dialer.DialerActivity")
    driver.execute_script('mobile: longClickGesture', {'x': 250, 'y': 270, 'duration': 1000})
    # can_swipe = driver.execute_script('mobile: swipeGesture', {
    #     "left", 100, "top", 100, "width", 200, "height", 332,
    #     "direction", "up",
    #     "percent", 1
    # })
    driver.find_element(AppiumBy.ID, "com.fossil.phone:id/tv_settings").click()

    time.sleep(10)
    driver.quit()
    # launchApp(app="/Users/pthanh2/Documents/AUTOMATION/0_HADO_FOSSIL/0_CODE/pythonThuPhamMobile/app/calculator.apk")
