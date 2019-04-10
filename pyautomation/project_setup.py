import yaml

config_file = {"application": {"username": "admin@phptravels.com", "password": "demoadmin"}, "webdriver": {"sauce": {"username": None, "key": None, "browserName": None, "caps": {"browserName": "chrome", "version": 66.0, "platform": "macOS 10.13"}}, "remote": {"url": None, "platform": None}, "type": "local", "chrome": {"driver": "C:\\chromedriver.exe", "arguments": ["--disable-extensions", "--headless"]}, "firefox": {"driver": "path", "preferences": {"browser.download.dir": "H:\\Downloads", "browser.download.manager.showWhenStarting": False}}, "wait": {"short": 10, "long": 30}, "implicit_wait": 10}, "tests": {"browser": {"name": "chrome", "scope": "class"}}, "api": {"request": {"timeout": 20}}}

page = '''
# @auther :generated by pyautomation
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyautomation.web.webpage import WebPage
from pyautomation.web.element import Element


class SearchPage(WebPage):

    def __init__(self, driver):
        self.driver = driver

    search_field = Element(By.NAME, "q")

    def load(self):
        self.driver.get("http://google.com")

    def is_loaded(self):
        pass

    def search(self, query):
        self.search_field.send_keys(query + Keys.ENTER)
'''

tests = '''
# @auther :generated by pyautomation
from tests.pages.search_page import SearchPage
from pyautomation.web.webtest import WebTest
from pyautomation.web.create_page import CreatePage
     
class TestSearch(WebTest):
    def test_search(self):
        page = CreatePage.get(SearchPage, self.driver)
        print(page.search_field.text)
        page.search("test")
        assert self.driver.title.startswith("test"), "title does not match"
        '''

api = '''
# @auther :generated by pyautomation
from pyautomation.api.request import Request, ContentType
import pytest


@pytest.mark.api
def test_post_request():
    # POST Request 
    headers = {
       'cache-control': "no-cache",
       'postman-token': "7f2e23ce-9c42-5184-6249-1a2031d95f45"
       } 
    response = Request().header(ContentType.URLENC).set_base_url("https://postman-echo.com/post").add_param("strange", "boom").add_headers(headers                                                                                                                 ).post("post")
    print(response.body)
 
@pytest.mark.api
def test_delete_request():
    # DELETE Request
    resp = Request().set_base_url("http://fakerestapi.azurewebsites.net").set_path_param("id", 20).delete("/api/Books/{id}")
    print(resp.body)

@pytest.mark.api
def test_put_request():
    # PUT Request
    req = """ {"ID":182,"Title":"vog","Description":"bwb","PageCount":786,"Excerpt":"jwmbtifn","PublishDate":"2019-03-24T11:46:01.452Z"} """
    resp = Request().header(ContentType.JSON).set_base_url("http://fakerestapi.azurewebsites.net").set_body(req).set_path_param("id", 20).put("/api/Books/{id}")
    print(resp.body)
'''
# importing the required modules 
import os 
import argparse 

# error messages 
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .txt file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."


def main(): 
    # create parser object 
    parser = argparse.ArgumentParser(description = "A text file manager!") 

    # defining arguments for parser object 
    parser.add_argument("-n", "--name", type = str, nargs = 1, 
                        metavar = "project_name", default = None, 
                        help = "project name.") 
    
    parser.add_argument("-d", "--directory", type = str, nargs = 1, 
                        metavar = "file_name", default = None, 
                        help = "Deletes the specified text file.")  

    # parse the arguments from standard input 
    args = parser.parse_args() 
    
    # calling functions depending on type of argument 
    if args.name != None: 
        project_name = args.name
        
    if args.directory is None:
        project_dir = os.getcwd()
    elif args.directory != None and os.path.isdir(args.directory[0]): 
        project_dir = args.directory[0]
    else:
        raise ValueError
    
    print("Creating project...")
    project = os.path.join(project_dir, project_name[0])
    os.mkdir(project)
    os.chdir(project)
    with open(".rootfile", 'w') as f:
        f.write("# created by pyautomation...\nDo not remove this file it used to get root directory.\nproject root directory can be changed by moving this file")
    config = os.path.join(project, "config")
    os.makedirs(config)
    os.makedirs(os.path.join(project, "testdata"))
    pages = os.path.join(project, "tests", "pages")
    os.makedirs(pages)
    test_suites = os.path.join(project, "tests", "test_suites")
    os.makedirs(test_suites)
    os.chdir(config)
    with open("default.yml", 'w') as f:
        yaml.dump(config_file, f, default_flow_style=False)
    os.chdir(pages)
    with open("__init__.py", "w") as f:
        f.write("# Page objects place in this directory")
    with open("search_page.py", "w") as f:
        f.write(page)
    os.chdir(test_suites)
    with open("__init__.py", "w") as f:
        f.write("# test_suites place in this directory")
    with open("test_search.py", "w") as f:
        f.write(tests)
    with open("test_api.py", "w") as f:
        f.write(api)
    os.chdir(os.path.join(project, "tests"))
    with open("__init__.py", "w") as f:
        pass
    print("project created successfully.")

if __name__ == "__main__": 
    # calling the main function 
    main() 
