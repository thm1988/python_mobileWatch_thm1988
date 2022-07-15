import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_launchApp(host="http://localhost:4723/wd/hub", udid="K6F1021084B0061", **kwargs):
    desired_caps = {'udid': udid, 'platformName': 'android', 'automationName': 'UiAutomator2'}
    desired_caps.update(kwargs)
    return webdriver.Remote(host, desired_caps)


if __name__ == '__main__':
    test_launchApp(
        app="/Users/pthanh2/Documents/AUTOMATION/0_HADO_FOSSIL/0_CODE/pythonThuPhamMobile/app/com.nike.plusgps.apk",
        appPackage="com.nike.plusgps", appActivity="com.nike.plusgps.activities.MainActivity")

    # launchApp(app="/Users/pthanh2/Documents/AUTOMATION/0_HADO_FOSSIL/0_CODE/pythonThuPhamMobile/app/calculator.apk")
