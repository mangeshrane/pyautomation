'''
Created on Apr 15, 2019

@author: mrane
'''

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