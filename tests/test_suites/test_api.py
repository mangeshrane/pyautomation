'''
Created on Feb 7, 2019
 
@author: mrane
'''
import pytest
from pyautomation.api.request import Request, ContentType
from pyautomation.assertion.delayed_assertions import Assertions

@pytest.fixture(scope="class")
def spec():
    request = Request().header(ContentType.JSON
                     ).set_base_url("https://jsonplaceholder.typicode.com")
    return request

def test_get_posts(spec):
    response = spec.get("/posts/1")
    print(response.body.userId)
    assertion = Assertions()
    assertion.expect(response.body.userId == 3)
    assertion.assert_expectations()
    print(response)
    
def test_post_request():
    # POST Request 
    headers = {
       'cache-control': "no-cache",
       'postman-token': "7f2e23ce-9c42-5184-6249-1a2031d95f45"
       } 
    response = Request().header(ContentType.URLENC).set_base_url("https://postman-echo.com/post").add_param("strange", "boom").add_headers(headers                                                                                                                 ).post("post")
    print(response.body)
   
def test_delete_request():
    # DELETE Request
    resp = Request().set_base_url("http://fakerestapi.azurewebsites.net").set_path_param("id", 20).delete("/api/Books/{id}")
    print(resp.body)
   
def test_put_request():
    # PUT Request
    req = ''' {"ID":182,"Title":"vog","Description":"bwb","PageCount":786,"Excerpt":"jwmbtifn","PublishDate":"2019-03-24T11:46:01.452Z"} '''
    resp = Request().header(ContentType.JSON).set_base_url("http://fakerestapi.azurewebsites.net").set_body(req).set_path_param("id", 20).put("/api/Books/{id}")
    print(resp.body)
   
def test_head_request():
    # HEAD Request
    pass
