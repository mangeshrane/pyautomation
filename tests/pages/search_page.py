from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyautomation.web.webpage import WebPage
from pyautomation.web.element import Element, Elements


class SearchPage(WebPage):

    def __init__(self, driver):
        self.driver = driver

    search_field = Element(By.NAME, "q", 0)

    def load(self):
        self.driver.get("http://google.com")

    def is_loaded(self):
        pass

    def search(self, query):
        self.search_field.send_keys(query + Keys.ENTER)

