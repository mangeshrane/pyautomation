import pytest

from pyautomation.configuration import CONFIG
from pyautomation.drivers.mobile_drivers import MobileDrivers
import subprocess
from pyautomation.logger.logger import LOG
import os


@pytest.mark.usefixtures("mobile")
class MobileTest:

    @pytest.fixture(scope=CONFIG.get("tests.mobile.scope", "class"))
    def mobile(self, request):
        """
        This fixture contains the set up and tear down code for each test.

        """
        drivers = MobileDrivers()
        try:
            LOG.info('starting appium server')
            process = subprocess.Popen('appium', shell=True)
            dev = CONFIG.get('tests.mobile.device_name', None)
            if drivers.MOBILE_CONFIG.get('platformName').lower() == 'android':
                if dev and CONFIG.get('tests.mobile.device_type', 'physical') == 'emulator':
                    LOG.info('starting emulator ' + dev)
                    try:
                        emulator = subprocess.Popen('emulator ' + dev)
                    except:
                        try:
                            emulator = subprocess.Popen([os.path.join(os.environ['ANDROID_HOME'],"emulator", "emulator.exe"), '-avd', dev], shell=True)
                        except:
                            LOG.error('Error while lauching android emulator')
                            LOG.error('please make sure you have emulator in path or ANDROID_HOME variable is set')
                            LOG.error('current ANDROID_HOME ' + os.environ['ANDROID_HOME'])
        except Exception as e:
            LOG.error(e)
        self.driver = drivers.mobile()
        request.cls.driver = self.driver
        yield 
        # Close browser window:
        self.driver.quit()
        process.terminate()
        emulator.terminate()
        LOG.info('Tear down completed')
        
