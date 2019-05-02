'''
Created on Apr 30, 2019

@author: mrane
'''
from pyautomation.mobile.mobile_test import MobileTest
from tests.selendroid_test_app.homepage import HomePage
from tests.selendroid_test_app.selendroid_test_app import TestApp
import time
from pyautomation.mobile.locator_type import UiSelector


class TestSelendroidApp(MobileTest):
    
    def test_accept_alert(self):
        homepage = HomePage(self.driver)
        homepage.click_localization_btn_and_accept_alert()
        time.sleep(5)
        assert self.driver.current_activity != TestApp(self.driver).activity_id(), "Alert not accepted"
    
    def test_dismiss_alert(self):
        homepage = HomePage(self.driver)
        homepage.click_localization_btn_and_dismiss_alert()
        el = self.driver.find_element_by_android_uiautomator(UiSelector().class_name('android.widget.Toast').locator)
        print(el)
        print(el.text)
        time.sleep(5)
        assert self.driver.current_activity == TestApp(self.driver).activity_id(), "Alert not dismissed"