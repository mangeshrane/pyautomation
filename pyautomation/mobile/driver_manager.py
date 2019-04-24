'''
Created on Apr 16, 2019

@author: mrane
'''
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyautomation import CONFIG
from appium import webdriver

class MobileDrivers(webdriver.Remote):
    
    def __init__(self):
        pass
    
    def get_android_driver(self):
        caps = DesiredCapabilities.ANDROID.copy();
        for key, value in CONFIG.get("android.capabilities"):
            caps[key] = value
        driver = webdriver.Remote(CONFIG.get("android.url"), caps)
        
        