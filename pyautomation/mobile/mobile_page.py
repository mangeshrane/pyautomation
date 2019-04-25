from appium import webdriver

'''
toggle airplane mode:

self.driver.open_notifications()
self.driver.find_element_by_xpath('//android.widget.Switch[@content-desc="Airplane mode"]').click()
self.driver.back()
'''
from pyautomation.mobile.keycodes import AndroidKeys
from pyautomation.logger.logger import LOG
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
    
    def accept_alert(self):
        return self.driver.execute_script("mobile:acceptAlert")
    
    def toggle_airplane_mode(self):
        self.driver.set_network_connection(1)
    
    def switch_apps(self, app_name):
        # Press Home Key
        self.driver.keyevent(AndroidKeys.HOME)
        # Open Recents app drawer
        self.driver.sendKeyEvent(AndroidKeys.RECENTS);
        # Tap our first app
        elem = self.driver.find_element_by_class_name("android.widget.FrameLayout")
        for i in elem:
            LOG.info("elem.get_attribute('name') :: " + i.get_attribute('name')) 
            if i.get_attribute('name') == app_name:
                LOG.info("Tapping :: " + i.get_attribute('name')) 
                self.driver.tap(1, elem.get(i), 100)
                break
        LOG.info("SWitched to app " + self.driver.current_activity)
            
