'''
Created on Feb 18, 2019

@author: mrane
'''
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as ffOptions
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os
from pyautomation.configuration import CONFIG
from pyautomation.logger.logger import LOG


class WebDrivers(object):

    @property
    def chrome(self, extension=None, headless=False):
        option = Options()
        option.headless = headless
        for arg in CONFIG.get("webdriver.chrome.arguments", []):
            option.add_argument(arg)
        if extension:
            option.add_extension(extension)
        if CONFIG.get("webdriver.type", "local") != "remote":
            driver = webdriver.Chrome(
                executable_path=CONFIG.get("webdriver.chrome.driver"),
                options=option)
        else:
            chrome_capabilities = webdriver.DesiredCapabilities.CHROME
            chrome_capabilities['platform'] = CONFIG.get("webdriver.remote.platform")
            chrome_capabilities['browserName'] = 'chrome'
            chrome_capabilities['javascriptEnabled'] = True
            driver = webdriver.Remote(
                    command_executor=CONFIG.get("webdriver.remote.url"),
                    desired_capabilities=webdriver.DesiredCapabilities.CHROME,
                    options=option)
        driver.implicitly_wait(CONFIG.get("webdriver.implicit_wait", 0))
        LOG.info("returning {0} chrome driver with {1}".format(CONFIG.get("webdriver.type", "local"), str(option)))
        return driver
    
    @property
    def firefox(self, args=[], extension=None):
        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        firefox_capabilities['platform'] = CONFIG.get("webdriver.remote.platform")
        firefox_capabilities['browserName'] = 'firefox'
        firefox_capabilities['javascriptEnabled'] = True
        firefox_capabilities['marionette'] = True

        options = ffOptions()
        options.log.level = 'trace'
            
        profile = FirefoxProfile()
        pref = CONFIG.get("webdriver.firefox.preferences", None)
        if pref:
            for key, value in pref.items():
                profile.set_preference(key, value)
        if extension:
            profile.add_extension(extension)
        if CONFIG.get("webdriver.type", "local") != "remote":
            driver = webdriver.Firefox(profile, executable_path=CONFIG.get("webdriver.firefox.driver"))
        else:
            driver = webdriver.Remote(command_executor=CONFIG.get("webdriver.remote.url"),
                                      desired_capabilities=firefox_capabilities, 
                                      options=options)
        LOG.info("returning {0} chrome driver with {1}".format(CONFIG.get("webdriver.type", "local"), str(profile)))
        return driver
    
    @property
    def sauce(self):
        driver = webdriver.Remote(
            command_executor="https://" + CONFIG.get("sauce.username") + ":" + CONFIG.get("sauce.key") + "@ondemand.saucelabs.com:443/wd/hub",
            desired_capabilities=CONFIG.get("webdriver.sauce.caps"))
        LOG.info("returning saurce remote webdriver")
        return driver
    
    @staticmethod
    def get():
        if os.environ.get("CORE.DRIVER", None):
            browser = os.environ["CORE.DRIVER"]
            LOG.info("getting browser from CORE.DRIVER : " + browser)
        else:
            browser = CONFIG.get("tests.browser.name", "chrome")
            LOG.warning("CORE.DRIVER not found setting browser : " + browser)
        return WebDrivers.__getattribute__(WebDrivers(), browser)
