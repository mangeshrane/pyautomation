import pytest
from pyautomation import CONFIG
from pyautomation.mobile.locator_type import UiAutomator

@pytest.mark.usefixtures("mobile")
class MobileTest():
    
    @pytest.fixture(scope=CONFIG.get("tests.mobile.scope", "class"))
    def web_driver(self, request):
        '''
        This fixture contains the set up and tear down code for each test.
        
        '''
        self.driver = WebDrivers().get()
        request.cls.driver = self.driver 
        driver.find_element_by_android_uiautomator(UiAutomator().checked("true").class_name(""))
        yield 
        # Close browser window:
        self.driver.quit()