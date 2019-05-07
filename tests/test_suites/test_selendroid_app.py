'''
Created on Apr 30, 2019

@author: mrane
'''
from pyautomation.mobile.mobile_test import MobileTest
from tests.selendroid_test_app.homepage import HomePage
from tests.selendroid_test_app.selendroid_test_app import TestApp
import time
from pyautomation.mobile.locator_type import UiSelector
from pytesseract import image_to_string
from pyautomation.mobile.mobile_element import MobileElement
from appium.webdriver.common.mobileby import MobileBy


class TestSelendroidApp(MobileTest):
#     
#     def test_accept_alert(self):
#         homepage = HomePage(self.driver)
#         homepage.click_localization_btn_and_accept_alert()
#         assert self.driver.current_activity != TestApp(self.driver).activity_id(), "Alert not accepted"
#     
#     def test_dismiss_alert(self):
#         homepage = HomePage(self.driver)
#         homepage.click_localization_btn_and_dismiss_alert()
# #         file = self.driver.get_screenshot_as_base64()
# #         print(image_to_string(file))
# #         assert self.driver.current_activity == TestApp(self.driver).activity_id(), "Alert not dismissed"
    
    def test_input_text(self):
        homepage = HomePage(self.driver)
#         homepage.input_box.send_keys("Test String")
#         self.driver.hide_keyboard()
# #         homepage.progress_bar_btn.click()
#         homepage.accept_adds_checkbox.click()
#         homepage.text_view_btn.click()
#         homepage.popup_btn.click()
#         self.driver.switch_to.alert.dismiss()
#         alert = self.driver.switch_to().alert()
#         alert.dismiss()
    