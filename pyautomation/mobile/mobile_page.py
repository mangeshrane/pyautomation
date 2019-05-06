'''
toggle airplane mode:

self.driver.open_notifications()
self.driver.find_element_by_xpath('//android.widget.Switch[@content-desc="Airplane mode"]').click()
self.driver.back()
'''

from appium import webdriver

class MobilePage(object):
    
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.driver.start_recording_screen()
    
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
    
    def is_checked(self, element):
        return element.get_attribute("checked").equals("true")

    def is_checkable(self, element):
        return element.get_attribute("checkable").equals("true")

    def is_clickable(self, element):
        return element.get_attribute("clickable").equals("true")

    def isEnabled(self, element):
        return element.get_attribute("enabled").equals("true")

    def isFocusable(self, element):
        return element.get_attribute("focusable").equals("true")

    def isFocused(self, element):
        return element.get_attribute("focused").equals("true")

    def isScrollable(self, element):
        return element.get_attribute("scrollable").equals("true")

    def isLongClickable(self, element):
        return element.get_attribute("longClickable").equals("true")

    def isSelected(self, element):
        return element.get_attribute("selected").equals("true")

    def getLocation(self, element):
        return element.getLocation()

    def getText(self, element):
        return element.get_attribute("name")

    def getResourceId(self, element):
        return element.get_attribute("resourceId")

    def getClassName(self, element):
        return element.get_attribute("className")

    def getContentDesc(self, element):
        return element.get_attribute("contentDesc")
