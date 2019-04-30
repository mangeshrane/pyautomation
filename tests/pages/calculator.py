'''
Created on Apr 29, 2019

@author: mrane
'''
from pyautomation.mobile.mobile_page import MobilePage
from pyautomation.mobile.mobile_element import MobileElement
from appium.webdriver.common.mobileby import MobileBy
from pyautomation.mobile.locator_type import UiSelector


class Calculator(MobilePage):
    
    def __init__(self, driver):
        self.driver = driver
    
    numeric_key = MobileElement(MobileBy.ANDROID_UIAUTOMATOR, UiSelector().resourceid("com.android.calculator2:id/digit_6").clickable('true'))