from pyautomation.mobile.mobile_test import MobileTest
from tests.pages.calculator import Calculator
import time

class TestMobile(MobileTest):
    
    def test_app_launch(self):
        page = Calculator(self.driver)
        page.numeric_key.click()
        page.switch_to_app("Gmail")
        time.sleep(6)