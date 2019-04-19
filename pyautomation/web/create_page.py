'''
Created on Feb 12, 2019

@author: mrane
'''
from selenium.common.exceptions import TimeoutException
from pyautomation.web.webpage import WebPage
from pyautomation.logger import LOG


class CreatePage(object):

    @staticmethod
    def get(page, driver):
        try:
            issubclass(page, WebPage)
        except AssertionError:
            LOG.error("Not a Page")
            raise AssertionError("Not a Page")
        return CreatePage._create_page(page, driver)
    
    @staticmethod
    def _create_page(page, driver, num=3):
        while num > 0:    
            pobject = page(driver)
            pobject.load()
            try:
                pobject.is_loaded()
                LOG.info("{} page is loaded".format(page.__name__))
                return pobject
            except AssertionError:
                CreatePage._create_page(page, driver, num=num-1)
            except TimeoutException:
                CreatePage._create_page(page, driver, num=num-1)
            else:
                break
        