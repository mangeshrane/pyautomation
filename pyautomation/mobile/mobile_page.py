from appium import webdriver

'''
toggle airplane mode:

self.driver.open_notifications()
self.driver.find_element_by_xpath('//android.widget.Switch[@content-desc="Airplane mode"]').click()
self.driver.back()
'''
from pyautomation.mobile.keycodes import AndroidKeys
from pyautomation.logger.logger import LOG
from pyautomation.mobile.locator_type import UiSelector
from appium.webdriver.common.touch_action import TouchAction
from pyautomation.configuration import CONFIG
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class MobilePage(object):
    
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
    
    def swipe(self):
        pass
    
    def get_text(self):
        pass
    
    def tap_element(self, element):
        pass
    
    def scroll_to(self, element):
        pass
    
    def move_to_element(self, element):
        pass
    
    def click_button(self, element):
        pass
    
    def wait_for_element_to_disappear(self, element):
        pass
    
    def scroll_to_element_and_click(self, element):
        pass
    
    def get_screen_height(self):
        return self.driver.get_window_size()["width"]
    
    def get_screen_width(self):
        return self.driver.get_window_size()["height"]
    
    def get_battery_info(self):
        return self.driver.execute_script("mobile:batteryInfo")
    
    def toggle_airplane_mode(self):
        self.driver.set_network_connection(1)
    
    def switch_to_app(self, app_name):
        # Press Home Key
        self.driver.keyevent(AndroidKeys.HOME)
        # Open Recents app drawer
        self.driver.keyevent(AndroidKeys.RECENTS)
        # Scroll into view
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("'+app_name+'"))')
        elem = self.driver.find_element_by_android_uiautomator(UiSelector().class_name("android.widget.ScrollView").clickable('false').locator)
        LOG.info("====== " + str(elem))
        elem = elem.find_elements_by_android_uiautomator(UiSelector().class_name('android.widget.FrameLayout').locator)
        LOG.info("====== " + str(elem))
        for i in elem:
            el = i.find_element_by_class_name("android.widget.TextView")
            LOG.info("elem.get_attribute('text') :: " + el.get_attribute('text')) 
            if el.get_attribute('text').lower() == app_name.lower():
                LOG.info("Tapping :: " + el.get_attribute('text')) 
                LOG.info("---------> " + str(i))
                TouchAction(self.driver).tap(i).perform()
                LOG.info("------> " + self.driver.current_package)
                if app_name.lower() not in self.driver.current_package:
                    self.driver.keyevent(AndroidKeys.RECENTS)
                break
        LOG.info("SWitched to app " + self.driver.current_activity)
     
#     def accept_alert(self, wait=CONFIG.get("webdriver.wait.short")):
#         """
#         Accepts the alert window
#         parameter:
#             wait: int [optional] 
#         """
#         try:
#             WebDriverWait(self.driver, wait).until(EC.alert_is_present(),
#                                                    'Timed out waiting for confirmation popup to appear.')
#             alert = self.driver.switch_to_alert()
#             alert.accept()
#             return True
#         except TimeoutException:
#             LOG.info('No alert accepted')
#             return False
