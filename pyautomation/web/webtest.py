'''
Created on Feb 28, 2019

@author: mrane
'''

import pytest
from pyautomation import CONFIG, LOG
from pyautomation.browsers.web_drivers import WebDrivers

@pytest.mark.usefixtures("web_driver")
class WebTest():
    
    @pytest.fixture(scope=CONFIG.get("tests.browser.scope", "class"))
    def web_driver(self, request):
        '''
        This fixture contains the set up and tear down code for each test.
        
        '''
        self.driver = WebDrivers().get()
        request.cls.driver = self.driver 
        yield 
        # Close browser window:
        self.driver.quit()
