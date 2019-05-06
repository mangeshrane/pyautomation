'''
Created on Feb 5, 2019

@author: mrane
'''
from abc import ABC, abstractmethod

from selenium.common.exceptions import TimeoutException,\
    StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pyautomation.web.element import Element
from pyautomation.configuration import CONFIG
from pyautomation.logger.logger import LOG
from selenium.webdriver.remote.webelement import WebElement



class WebPage(ABC):
    """
    Base class that all page models can inherit.
    This class contains useful methods for UI automation
    """
    
    def __init__(self, driver):
        """
        parameters:
            driver: webdriver instance
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
    
    def refresh(self):
        self.driver.refresh()
    
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
            element: Element 
        """
        ActionChains().move_to_element(element)
    
    def get_dropdown(self, element):
        """
            returns a dropdown
        """
        return Select(element)
    
    def click_element_with_js(self, element):
        """
        performs click on a element using Javascript
        """
        self.driver.execute_script("arguments[0].click()", element)

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

    def clear_and_send_keys(self, element: WebElement, keys):
        """
        clears default value and sends key to the element
        """
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

    def wait_for_element_to_be_present(self, element, timeout=10):
 
        """
        This method is used for explicit waits till element present
        :param element: Element
        :param timeout: time to wait for
        :return: boolean
        """
        try:
            WebDriverWait(self.driver, timeout, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.presence_of_element_located((element.__dict__['_by'], element.__dict__['_locator']))
            )
            return True
        except:
            LOG.error("Timeout while waiting for element to present")
            return False
    
    def wait_for_element_to_be_clickable(self, element, timeout=10):

        """
        This function is used for explicit waits till element clickable
        :param element: Element
        :param timeout: time to wait for
        :return: boolean
        """
        try:
            WebDriverWait(self.driver, timeout, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.element_to_be_clickable((element.__dict__['_by'], element.__dict__['_locator']))
            )
            return True
        except:
            LOG.error("Exception occurred while waiting for element to be clickable.")
            return False

    def wait_for_element_to_be_displayed(self, element, timeout=10):

        """
        This function is used for explicit waits till element displayed
        :param element: Element
        :param timeout: time to wait for
        :return: boolean
        """
        try:
            WebDriverWait(self.driver, timeout, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.visibility_of_element_located((element.__dict__['_by'], element.__dict__['_locator']))
            )
            return True
        except:
            self.log.error("Exception occurred while waiting for element to be visible.")
            return False

    def wait_for_element_to_be_invisible(self, element, timeout=10):

        """
        This function is used for explicit waits till element displayed
        :param element: Element
        :param timeout: time to wait for
        :return: boolean
        """
        try:
            WebDriverWait(self.driver, timeout, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.invisibility_of_element_located((element.__dict__['_by'], element.__dict__['_locator']))
            )
            return True
        except:
            return False

    def is_element_present(self, element, timeout=10):

        """
        This method is used to return the boolean value for element present
        :param element: Element
        :param timeout: time to wait for
        :return: boolean
        """
        flag = False
        try:
            if self.wait_for_element_to_be_present(element, timeout):
                flag = True
            else:
                LOG.error(
                    "Element not present with locator_properties: " + element.__dict__['_by'] + " =" + element.__dict__['_locator'])
        except:
            LOG.error("Exception occurred during element identification.")
        return flag

    def verify_element_not_present(self, element, timeout=10):

        """
        This method is used to return the boolean value for element present
        :param element: Element
        :param timeout: time to wait for
        :return: boolean
        """
        flag = False
        try:
            if self.wait_for_element_to_be_invisible(element, timeout):
                LOG.info(
                    "Element invisible with locator_properties: " + element.__dict__['_by'] + "= " + element.__dict__['_locator'])
                flag = True
            else:
                LOG.error(
                    "Element is visible with locator_properties: " + element.__dict__['_by'] + "= " + element.__dict__['_locator'])
        except:
            LOG.error("Exception occurred during element to be invisible.")
        return flag

    def is_element_displayed(self, element, timeout=10):

        """
        This method is used to return the boolean value for element displayed
        :param element: Element
        :param timeout: time to wait for
        :return: boolean
        """
        try:
            if self.wait_for_element_to_be_displayed(element, timeout):
                LOG.info(
                    "Element found with locator_properties: " + element.__dict__['_by'] + "= " + element.__dict__['_locator'])
                return True
            else:
                LOG.error(
                    "Element not found with locator_properties: " + element.__dict__['_by'] + "= " + element.__dict__['_locator'])
                return False
        except:
            self.log.error("Exception occurred during element identification.")
            return False

    def is_element_clickable(self, element, timeout=10):

        """
        This method is used to return the boolean value for element clickable
        :param element: Element
        :param timeout: time to wait for
        :return: boolean
        """
        try:
            if self.wait_for_element_to_be_clickable(element, timeout):
                LOG.info(
                    "Element is clickable with locator_properties: " + element.__dict__['_by'] + " =" + element.__dict__['_locator'])
                return True
            else:
                LOG.error(
                    "Element is not clickable with locator_properties: " + element.__dict__['_by'] + " =" + element.__dict__['_locator'])
                return False
        except:
            LOG.error("Exception occurred during element identification.")
            return False

    def is_element_checked(self, element, timeout=10):

        """
        This method is used to return the boolean value for element checked/ selected
        :param element: Element
        :param timeout: time to wait for
        :return: boolean
        """
        flag = False
        try:
            if self.is_element_present(element, timeout):
                element = self.get_element(element, timeout)
                if element.is_selected():
                    LOG.info(
                        "Element is selected/ checked with locator_properties: " +
                        element.__dict__['_by'] + " =" + element.__dict__['_locator'])
                    flag = True
                else:
                    self.log.error(
                        "Element is not selected/ checked with locator_properties: " +
                        element.__dict__['_by'] + " =" + element.__dict__['_locator'])
        except:
            flag = False

        return flag
    
    def scroll_up(self):
        """
        This methos is used for page scrolling
        :param direction: it takes the scrolling direction value as parameter
        :return: it returns nothing
        """
        self.driver.execute_script("window.scrollBy(0, -1000);")

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")
    