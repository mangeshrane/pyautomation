'''
Created on Apr 22, 2019

@author: mrane
'''
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium import webdriver
from pyautomation.configuration import CONFIG


class MobileDrivers:

    @staticmethod
    def mobile() -> webdriver.Remote:
        caps = DesiredCapabilities.ANDROID.copy()
        config = CONFIG.get("mobile.capabilities").items()
        for key, value in config:
            caps[key] = value
        driver = webdriver.Remote(CONFIG.get("android.url"), caps)
        return driver
