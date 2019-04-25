'''
Created on Feb 5, 2019

@author: mrane
'''
from abc import ABC, abstractmethod

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pyautomation.web.element import Element
from pyautomation.configuration import CONFIG
from pyautomation.logger.logger import LOG



class WebPage(ABC):
    """
    Base class that all page models can inherit.
    This class contains useful methods for UI automation
    """
    
    def __init__(self, driver):
        """
        parameters:
            driver: webdriver instance
            implicit_wait: [optional] default=10
        """
        self.base_url = CONFIG.get("application.url", "")
        super().__init__(driver)
        self.driver = driver

    def _load(self, url):
        url = self.base_url + url
        self.driver.get(url)
    
    @abstractmethod
    def load(self):
        """
        Abstract methods needs to be implemented by pages
        will be called to instantiate the page
        usage:
            
            def load(self):
                self.driver.get("http://google.com")
                
        """
        pass

    @abstractmethod
    def is_loaded(self):
        """
        Abstract methods needs to be implemented by pages
        will be called to instantiate the page
        usage:
        
            def is_loaded(self):
                assert self.loginBtn.is_displayed(), "Not displayed"
        """
        pass
    
    def wait_for_multiple_windows(self):
        """
        test will wait to open one or more windows
        """
        handles = self.driver.window_handles
        while handles < 0:
            handles = self.driver.window_handles

    def switch_to_window(self, index):
        """
        Switches the windows to given index
        
        parameters:
            index: int -> window index to switch to
        """
        try:
            self.driver.switch_to.window(self.driver.window_handles[index])
        except IndexError:
            LOG.error("window handle index out of bound")
    
    def switch_to_last_window(self):
        """
        switches to last indexed window
        """
        self.driver.switch_to_window(-1)
            
    def switch_to_first_window(self):
        """
        switches to first indexed window
        """
        self.driver.switch_to_window(0)
        
    def move_to_element(self, element):
        """
        moves the mouse to element
        
        parameters:
            element: Element type->core.page.Element
        """
        if isinstance(element, Element):
            ActionChains().move_to_element(element)
        else:
            raise AttributeError("element should be of Element type")
            LOG.error("element should be of Element type")
    
    def get_dropdown(self, element):
        """
            returns a dropdown
        """
        return Select(element)
    
    def click_element_with_js(self, element):
        """
        performs click on a element using Javascript
        """
        if isinstance(element, Element):
            self.driver.execute_script("arguments[0].click()", element)
        else:
            raise AttributeError("element should be of Element type")
            LOG.error("element should be of Element type")

    def click_and_hold(self, element):
        """
        performs click and hold on a element
        
        parameters:
            element: Element
        """
        ActionChains(self.driver).click_and_hold(element).perform()

    def upload_file(self, element, filepath):
        """
        uploads file
        parameter:
            element: Element
            filepath: str [file location]
            
        """
        element.send_keys(filepath)

    def accept_alert(self, wait=CONFIG.get("webdriver.wait.short")):
        """
        Accepts the alert window
        parameter:
            wait: int [optional] 
        """
        try:
            WebDriverWait(self.driver, wait).until(EC.alert_is_present(),
                                                   'Timed out waiting for confirmation popup to appear.')
            alert = self.driver.switch_to_alert()
            alert.accept()
            return True
        except TimeoutException:
            LOG.info('No alert accepted')
            return False

    def press_enter_key(self, loc):
        """
        sends enter key to element
        """
        if isinstance(loc, Element):
            loc.send_keys(Keys.ENTER)
        else:
            raise AttributeError("loc must be of Element type")

    def clear_and_send_keys(self, element, keys):
        """
        clears default value and sends key to the element
        """
        if isinstance(element, Element):
            pass
        else:
            raise ValueError("Needed element of type Element")
        element.click()
        element.clear()
        element.send_keys(keys)

    def go_back(self):
        """
        navigates to back
        """
        self.driver.back()

    def dismiss_alert(self, wait=CONFIG.get("webdriver.wait.short")):
        """
        dismisses the alert window
        parameter: 
            wait: int [default= webdriver.wait.short in config file]
        """
        try:
            WebDriverWait(self.driver, wait).until(EC.alert_is_present(),
                                                   'Timed out waiting for confirmation popup to appear.')
            alert = self.driver.switch_to_alert()
            alert.dismiss()
        except TimeoutException:
            print('No alert dismissed')
    
    def is_page_loaded(self):
        """
        checks if page if loaded using javascript 
        returns -> boolean
        """
        self.driver.execute_script('return document.readyState == "complete"')
    
    def assert_page_contains(self, string):
        """
        asserts if given string is in the webpage
        """
        assert string in self.driver.page_source, "Content doesn't match. Message is {0}".format(string)

