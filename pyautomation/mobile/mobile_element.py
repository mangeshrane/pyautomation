'''
Created on Apr 15, 2019

@author: mrane
'''
from pyautomation.mobile.locator_type import UiAutomator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyautomation import LOG

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
        if isinstance(locator, UiAutomator):
            self._locator = locator.locator
        else:
            self._locator = locator
        self._wait = wait
        

    def __get__(self, instance, owner):
        if self._wait:
            return WebDriverWait(instance.driver, self._wait).until(
                EC.presence_of_element_located((self._by, self._locator)))
        else:
            return instance.driver.find_element(self._by, self._locator)
        LOG.info("returning element {}={} ".format(self._by, self._locator))

    def __set__(self, instance, name):
        pass

    def __delete__(self):
        pass
    
    def is_checked(self):
        return self.__get__(self, None).getAttribute("checked").equals("true")

    def is_checkable(self):
        return self.__get__(self, None).getAttribute("checkable").equals("true")

    def is_clickable(self):
        return self.__get__(self, None).getAttribute("clickable").equals("true")

    def isEnabled(self):
        return self.__get__(self, None).getAttribute("enabled").equals("true");

    def isFocusable(self):
        return self.__get__(self, None).getAttribute("focusable").equals("true");

    def isFocused(self):
        return self.__get__(self, None).getAttribute("focused").equals("true");

    def isScrollable(self):
        return self.__get__(self, None).getAttribute("scrollable").equals("true");

    def isLongClickable(self):
        return self.__get__(self, None).getAttribute("longClickable").equals("true");

    def isSelected(self):
        return self.__get__(self, None).getAttribute("selected").equals("true");

    def getLocation(self):
        return self.__get__(self, None).getLocation();

    def getText(self):
        return self.__get__(self, None).getAttribute("name");

    def getResourceId(self):
        return self.__get__(self, None).getAttribute("resourceId");

    def getClassName(self):
        return self.__get__(self, None).getAttribute("className");

    def getContentDesc(self):
        return self.__get__(self, None).getAttribute("contentDesc");
    
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
        if isinstance(locator, UiAutomator):
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