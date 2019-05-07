import os
import subprocess
import time

import pytest

from pyautomation.configuration import CONFIG
from pyautomation.drivers.mobile_drivers import MobileDrivers
from pyautomation.logger.logger import LOG
from pyautomation.mobile.adb import Adb


@pytest.mark.usefixtures("mobile")
class MobileTest:

    @pytest.fixture(scope=CONFIG.get("tests.mobile.scope", "class"))
    def mobile(self, request):
        """
        This fixture contains the set up and tear down code for each test.

        """
        emu = set(Adb.get_connected_devices())
        LOG.info('Connected devices ' + str(emu))
        drivers = MobileDrivers()
        try:
            LOG.info('starting appium server')
            process = subprocess.Popen('appium', shell=True)
            dev = CONFIG.get('tests.mobile.device_name', None)
            if drivers.MOBILE_CONFIG.get('capabilities.platformName').lower() == 'android':
                if dev and CONFIG.get('tests.mobile.device_type', 'physical') == 'emulator':
                    LOG.info('starting emulator ' + dev)
                    try:
                        subprocess.Popen([os.path.join(os.environ['ANDROID_HOME'], "emulator", "emulator.exe"), '-avd', dev], shell=True)
                        time.sleep(5)
                    except:
                        LOG.error('Error while lauching android emulator')
                        LOG.error('please make sure you have emulator in path or ANDROID_HOME variable is set')
                        LOG.error('current ANDROID_HOME ' + os.environ['ANDROID_HOME'])
                    emu_n = set(Adb.get_connected_devices())
                    LOG.info('Connected devices ' + str(emu_n))
                    new_d = emu_n - emu
                    LOG.info('started emulator ' + str(new_d))
        except Exception as e:
            LOG.error(e)
        self.driver = drivers.mobile()
        request.cls.driver = self.driver
        yield 
        self.driver.quit()
        process.terminate()
        Adb.kill_emulator(new_d.pop())
        LOG.info('Tear down completed')
