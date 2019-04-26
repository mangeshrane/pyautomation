'''
Created on Feb 11, 2019

@author: mrane
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyautomation.logger.logger import LOG


class Element(object):
    '''
    WebElement descriptor to define webelements in page objects
    This will returns Webelement when it is accessed
    '''

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
        self._locator = locator
        self._wait = wait

    def __get__(self, instance, owner):
        element = None
        if self._wait:
            element = WebDriverWait(instance.driver, self._wait).until(
                EC.presence_of_element_located((self._by, self._locator)))
        else:
            element =  instance.driver.find_element(self._by, self._locator)
        LOG.info("returning element {}={} ".format(self._by, self._locator))
        element.__dict__['_by'] = self._by
        element.__dict__['_locator'] = self._locator
        return element
    
    def __set__(self, instance, name):
        pass

    def __delete__(self):
        pass


class Elements(object):
    '''
    WebElement descriptor to define webelements in page objects
    '''

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
        self._locator = locator
        self._wait = wait
        self._elements = None

    def __get__(self, instance, owner):
        if self._wait > 0:
            self.elements = WebDriverWait(instance.driver, self._wait).until(
                EC.presence_of_all_elements_located((self._by, self._locator)))
        else:
            self.elements = instance.driver.find_elements(self._by, self._locator)
        LOG.info("returning element {}={} ".format(self._by, self._locator))
        return self.elements    
        
    def __set__(self, instance, name):
        pass

    def __delete__(self):
        pass
