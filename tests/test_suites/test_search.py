from tests.pages.search_page import SearchPage
     
import allure
import pytest
import time
from pyautomation.web.webtest import WebTest
from pyautomation.web.create_page import CreatePage
from selenium import webdriver
from pyautomation.project_setup import page
     
     
@allure.story("User story")
@allure.feature("feature name")
class TestSearch(WebTest):
       
    # USING GROUPS eg. 'smoke'
    @pytest.mark.smoke
    def test_search(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        page = CreatePage.get(SearchPage, self.driver)
        page.search("test")
        time.sleep(2)
        page.scroll_down()
        time.sleep(2)
        page.scroll_up()
#         field = page.search_field
#        
#         time.sleep(2)
#         print(page.search_field)
#         page.refresh()
#         assert self.driver.title.startswith("test"), "title does not match"

TestSearch().test_search()