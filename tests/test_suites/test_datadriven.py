'''
Created on Mar 28, 2019
 
@author: mrane
'''
import pytest
from tests.pages.search_page import SearchPage
from pyautomation.web.webtest import WebTest
from pyautomation.web.create_page import CreatePage
from pyautomation.data_providers.csv_reader import CSVReader
from pyautomation.data_providers.excel_reader import ExcelReader
from pyautomation.data_providers.json_reader import JSONReader
  
class TestDatadriven(WebTest):
     
    # parametrize by specifying in tests
    @pytest.mark.parametrize("query, test", [('selenium',0), ('QTP',1)])
    def test_search_1(self, query, test):
        page = CreatePage.get(SearchPage, self.driver)
        page.search(query)
        assert self.driver.title.startswith(query), "title does not match"
            
    # parametrize using csv file
    @pytest.mark.parametrize(*CSVReader.get_data("users.csv", fields=["first_name", "last_name"]))
    def test_params_from_csv(self, first_name, last_name):
        print(first_name, last_name)
      
    # parametrize using excel file
    @pytest.mark.parametrize(*ExcelReader.get_data("data.xlsx", data_filter="Add Customer", fields=["firstName", "lastName"]))
    def test_params_from_xls(self,firstName, lastName):
        print(firstName, lastName)
       
    # parametrize using excel file without fields parametr
    @pytest.mark.parametrize(*ExcelReader.get_data("data.xlsx", data_filter="Add Admin"))
    def test_params_from_xls_1(self,firstName, lastName, email, password):
        print(firstName, lastName, email, password)
          
    # parametrize using json file
    @pytest.mark.parametrize(*JSONReader.get_data("data.json"))
    def test_params_from_json(self, name, role):
        print(name, role)
