import pytest

from pyautomation.configuration import CONFIG
from pyautomation.drivers.mobile_drivers import MobileDrivers


@pytest.mark.usefixtures("mobile")
class MobileTest:

    @pytest.fixture(scope=CONFIG.get("tests.mobile.scope", "class"))
    def mobile(self, request):
        """
        This fixture contains the set up and tear down code for each test.

        """
        self.driver = MobileDrivers.mobile()
        request.cls.driver = self.driver
        yield 
        # Close browser window:
        self.driver.quit()
