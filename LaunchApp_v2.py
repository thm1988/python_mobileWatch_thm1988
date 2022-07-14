import unittest
from appium import webdriver


class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        self.dc['app'] = "/Users/pthanh2/Documents/AUTOMATION/0_HADO_FOSSIL/0_CODE/pythonThuPhamMobile/app/calculator" \
                         ".apk"
        # appPackage and appActivity  desired capability specify app details to Appium
        self.dc['appPackage'] = "com.nike.plusgps"
        self.dc['appActivity'] = "com.nike.plusgps.activities.MainActivity"
        self.dc['platformName'] = "android"
        self.dc['deviceName'] = "K6F1081454B3395"
        self.dc['automationName'] = "UiAutomator2"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def testAppLaunch(self):
        el = self.driver.find_element_by_accessibility_id('com.nike.plusgps:id/login_text')
        el.click()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
