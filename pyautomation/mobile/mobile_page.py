from appium.webdriver.webdriver import WebDriver

'''
toggle airplane mode:

self.driver.open_notifications()
self.driver.find_element_by_xpath('//android.widget.Switch[@content-desc="Airplane mode"]').click()
self.driver.back()
'''
class MobilePage(object):
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
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
    
