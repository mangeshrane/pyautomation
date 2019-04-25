import pytest
from pyautomation import CONFIG
from appium import webdriver

@pytest.mark.usefixtures("mobile")
class MobileTest():
    
    @pytest.fixture(scope=CONFIG.get("tests.mobile.scope", "class"))
    def mobile(self, request):
        '''
        This fixture contains the set up and tear down code for each test.
        
        '''
        config = CONFIG.get("mobile.capabilities").items()
        for key, value in config:
            if not value:
                del config[key]
        self.driver = webdriver.Remote(CONFIG.get("mobile.remote.url"), config)
        request.cls.driver = self.driver 
        yield 
        # Close browser window:
        self.driver.quit()