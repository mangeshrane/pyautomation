'''
Created on Apr 22, 2019

@author: mrane
'''
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium import webdriver
from pyautomation.configuration import CONFIG


class MobileDrivers():
    
    def android(self):
        caps = DesiredCapabilities.ANDROID.copy();
        caps["browserName"]: "Safari"
        caps["deviceName"]: "iPhone 6 Device"
        caps["platformVersion"]: "8.4"
        caps['no-reset'] = 'true'
        caps['full-reset'] = 'False'
        caps = DesiredCapabilities.ANDROID.copy();
        for key, value in CONFIG.get("android.capabilities"):
            caps[key] = value
        driver = webdriver.Remote(CONFIG.get("android.url"), caps)