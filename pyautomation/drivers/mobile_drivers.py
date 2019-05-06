'''
Created on Apr 22, 2019

@author: mrane
'''
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium import webdriver

from pyautomation.configuration import CONFIG
import os
from pyautomation.logger.logger import LOG
from pyautomation.configuration.config_reader import Config


class MobileDrivers:
    
    def __init__(self):
        if os.environ.get("MOBILE.DEVICE", None):
            mobile_device = os.environ["MOBILE.DEVICE"]
            LOG.info("getting browser from MOBILE.DEVICE : " + mobile_device)
        else:
            mobile_device = CONFIG.get("tests.mobile.device_name", "test")
            LOG.warning("MOBILE.DEVICE not found setting device : " + mobile_device)
        try:
            self.MOBILE_CONFIG = Config(mobile_device + '.yml')
            LOG.info('loaded MOBILE_CONFIG ' + self.MOBILE_CONFIG)
        except:
            LOG.error('Unable to get config file named ' + mobile_device )
            LOG.error('Please specify config file in config folder named ' + mobile_device + ' with desired configuration')
    
    def mobile(self) -> webdriver.Remote:
        caps = DesiredCapabilities.ANDROID.copy()
        LOG.info('Checking if device is connected')
        #TODO
        LOG.info(self.MOBILE_CONFIG.get('appium'))
        config = self.MOBILE_CONFIG.get("capabilities").items()
        for key, value in config:
            caps[key] = value
        if CONFIG.get('tests.mobile.device_id', None):
            caps['udid'] = CONFIG.get('tests.mobile.device_id')
        driver = webdriver.Remote(self.MOBILE_CONFIG.get("appium.url"), caps)
        return driver
