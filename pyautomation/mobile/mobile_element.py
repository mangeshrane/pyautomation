'''
Created on Apr 15, 2019

@author: mrane
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyautomation.mobile.locator_type import UiSelector
from pyautomation.logger.logger import LOG

class MobileElement(object):
    
    def __init__(self, by, locator, wait=10):
        '''
        Constructor: 
        Parameters:
        ---------- 
        by : selenium.webdriver.common.by.By
        locator: string locator value
        wait: [optional] default=10
        
        '''
        self._by = by
        if isinstance(locator, UiSelector):
            self._locator = locator.locator
        else:
            self._locator = locator
        self._wait = wait
        

    def __get__(self, instance, owner):
        if self._wait:
            element = WebDriverWait(instance.driver, self._wait).until(
                EC.presence_of_element_located((self._by, self._locator)))
        else:
            element = instance.driver.find_element(self._by, self._locator)
        element.__dict__['_by'] = self._by
        element.__dict__['_locator'] = self._locator
        LOG.info("returning element {}={} ".format(self._by, self._locator))
        return element

    def __set__(self, instance, name):
        pass

    def __delete__(self):
        pass
    
class MobileElements(object):
    
    def __init__(self, by, locator, wait=10):
        '''
        Constructor: 
        Parameters:
        ---------- 
        by : selenium.webdriver.common.by.By
        locator: string locator value
        wait: [optional] default=10
        
        '''
        self._by = by
        if isinstance(locator, UiSelector):
            self._locator = locator.locator
        else:
            self._locator = locator
        self._wait = wait
        

    def __get__(self, instance, owner):
        if self._wait:
            return WebDriverWait(instance.driver, self._wait).until(
                EC.presence_of_all_elements_located((self._by, self._locator)))
        else:
            return instance.driver.find_elements(self._by, self._locator)
        LOG.info("returning element {}={} ".format(self._by, self._locator))

    def __set__(self, instance, name):
        pass

    def __delete__(self):
        pass