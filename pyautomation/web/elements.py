'''
Created on Feb 13, 2019

@author: mrane
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyautomation import LOG


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
                EC.presence_of_element_located((self._by, self._locator)))
        else:
            self.elements = instance.driver.find_elements(self._by, self._locator)
        LOG.info("returning element {}={} ".format(self._by, self._locator))
        return self.elements    
        
    def __set__(self, instance, name):
        pass

    def __delete__(self):
        pass
    
    @property
    def count(self):
        """
        returns count of elements
        """
        return len(self.__get__(self, None))
    
    def get_nth_element(self, number):
        """
        returns elements of at index specified
        
        parameters:
            number: int
        """
        try:
            if self._elements:
                self._elements[number]
            else:
                self._elements = self.__get__(self, None)
                self._elements[number]
        except IndexError:
            LOG.warning("Index Error occured while getting element")
            return None
        
    def get_last_element(self):
        """
        returns last element from elements
        """
        return self.get_nth_element(-1)
    
    def get_first_element(self):
        """
        returns first webelement of specified locator
        """
        return self.get_nth_element(0)
