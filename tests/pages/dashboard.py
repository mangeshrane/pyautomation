'''
Created on Feb 11, 2019

@author: mrane
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pyautomation.web.webpage import WebPage
from pyautomation.web.element import Element
from pyautomation.configuration import CONFIG


class Dashboard(WebPage):
    '''
    classdocs
    '''
    accounts = Element(By.XPATH,
                       "//body/div[@class='wrapper']/aside[@class='social-sidebar']/div/div[6]/div[@class='menu-content']/ul[@id='social-sidebar-menu']//a[@href='#ACCOUNTS']",
                       10)

    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver

    def load(self):
        pass

    def is_loaded(self):
        assert WebDriverWait(self.driver, CONFIG.get("webdriver.wait.long", 20)).until(
            expected_conditions.title_is("Dashboard"), "Title does not match")

    def click_on_accounts(self):
        self.accounts.click()
