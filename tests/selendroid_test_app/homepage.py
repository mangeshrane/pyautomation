'''
Created on Apr 30, 2019

@author: mrane
'''
from pyautomation.mobile.mobile_page import MobilePage
from pyautomation.mobile.mobile_element import MobileElement
from appium.webdriver.common.mobileby import MobileBy
from pyautomation.mobile.locator_type import UiSelector
from selenium.webdriver.common.by import By
from tests.selendroid_test_app.selendroid_test_app import TestApp

class HomePage(MobilePage, TestApp):
    
    def __init__(self, driver):
        self.driver = driver
        self.open()
    
    localization_btn = MobileElement(MobileBy.ANDROID_UIAUTOMATOR, UiSelector().resourceid('io.selendroid.testapp:id/buttonTest'))
    selendoid_webview = MobileElement(MobileBy.ANDROID_UIAUTOMATOR, UiSelector().resourceid('io.selendroid.testapp:id/buttonStartWebview'))
    registration_btn = MobileElement(By.XPATH, '//android.widget.ImageButton[@content-desc="startUserRegistrationCD"]')
    input_box = MobileElement(By.ID, 'io.selendroid.testapp:id/my_text_field')
    progress_bar_btn = MobileElement(MobileBy.ACCESSIBILITY_ID, 'waitingButtonTestCD')
    accept_adds_checkbox = MobileElement(MobileBy.ANDROID_UIAUTOMATOR, UiSelector().resourceid('io.selendroid.testapp:id/input_adds_check_box'))
    text_view_btn = MobileElement(MobileBy.ANDROID_UIAUTOMATOR, UiSelector().resourceid('io.selendroid.testapp:id/visibleButtonTest'))
    toast_btn = MobileElement(MobileBy.ANDROID_UIAUTOMATOR, UiSelector().resourceid('io.selendroid.testapp:id/showToastButton'))
    popup_btn = MobileElement(MobileBy.ANDROID_UIAUTOMATOR, UiSelector().resourceid('io.selendroid.testapp:id/showPopupWindowButton'))
    exception_btn = MobileElement(MobileBy.ANDROID_UIAUTOMATOR, UiSelector().resourceid('io.selendroid.testapp:id/exceptionTestButton'))
    input_exception = MobileElement(MobileBy.ANDROID_UIAUTOMATOR, UiSelector().resourceid('io.selendroid.testapp:id/exceptionTestField'))
    
    alert_agree = MobileElement(MobileBy.ANDROID_UIAUTOMATOR, UiSelector().resourceid('android:id/button1').text('I agree'))
    alert_dismiss = MobileElement(MobileBy.ANDROID_UIAUTOMATOR, UiSelector().resourceid('android:id/button2').text('No, no'))
    
    def click_localization_btn_and_accept_alert(self):
        self.localization_btn.click()
        self.alert_agree.click()
        
    def click_localization_btn_and_dismiss_alert(self):
        self.localization_btn.click()
        self.alert_dismiss.click()