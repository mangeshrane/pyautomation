'''
Created on Mar 14, 2019
  
@author: mrane
'''
from tests.pages.LoginPage import LoginPage
from pyautomation.web.webtest import WebTest
from pyautomation.web.create_page import CreatePage
from pyautomation.configuration import CONFIG
from pyautomation.logger.logger import LOG
  
class TestLoginPage(WebTest):
    '''
    classdocs
    '''
  
    def test_login(self):
        print("running login")
        page = CreatePage.get(LoginPage, self.driver)
        page = page.login(CONFIG.get("application.username"), CONFIG.get("application.password"))
        LOG.info("PAGE TITLE " + self.driver.title)
  
#     def test_accounts(self):
#         page = CreatePage.get(Dashboard, self.driver)
#         page.click_on_accounts()
#         time.sleep(5)

