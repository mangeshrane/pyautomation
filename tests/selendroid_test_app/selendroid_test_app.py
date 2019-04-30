'''
Created on Apr 30, 2019

@author: mrane
'''
from pyautomation.mobile.application import Application
from appium import webdriver

class TestApp(Application):
    
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
    
    def force_stop(self):
        self.driver.close_app()
    
    def clear_data(self):
        self.driver.reset()
    
    def open(self):
        self.driver.start_activity(self.package_id(), self.activity_id())
    
    def package_id(self):
        return 'io.selendroid.testapp'
    
    def activity_id(self):
        return 'io.selendroid.testapp.HomeScreenActivity'