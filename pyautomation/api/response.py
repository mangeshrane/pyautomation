'''
Created on Mar 20, 2019

@author: mrane
'''
import json

from requests.models import Response as rp
from collections import namedtuple
from pprint import pformat
import allure

ALLURE_RESP_TML = '<p> <h> <b> URL: </b> </h> {0}</p><p> <h> <b> Body<br> </b> </h> {1}</p><p> <h> <b> Headers<br> </b> </h> {2}</p><p> <h> <b> cookies<br> </b> </h> {3}</p><p> <h> <b> Status Code<br> </b> </h> {4}</p>'


class Response(object):
    '''
    classdocs
    '''

    def __init__(self, response):
        '''
        Constructor
        '''
        print("API Response body : \n\t" + pformat(str(response.text)))
        print("API Response headers : \n\t" + pformat(str(response.headers)))
        print("API Response cookies : \n\t" + pformat(str(response.cookies)))
        print("API Response status code : \n\t" + pformat(str(response.status_code)))
        allure.attach(
            ALLURE_RESP_TML.format(pformat(str(response.url)),
                                   pformat(str(response.text)),
                                   pformat(str(response.headers)),
                                   pformat(str(response.cookies)),
                                   pformat(str(response.status_code))
                                   ),
            'Response',
            allure.attachment_type.HTML)
        if not isinstance(response, rp):
            raise ValueError
        self.url = response.url
        self.status_code = response.status_code
        self._request = response.request
        try:
            self.body = PyJSON(response.text)
        except Exception:
            self.body = None
        self.reason = response.reason
        self.cookies = response.cookies
        self.headers = response.headers

    def assert_response_code(self, response_code):
        assert self.status_code == response_code, "Response code does not match, expected {0} but found {1}".format(
            response_code, self.status_code)
        return self

    def _json_object_hook(self, d):
        return namedtuple('response', d.keys())(*d.values())

    def json2obj(self, data):
        return json.loads(data, object_hook=self._json_object_hook)
    
    def assert_status_code(self, status_code):
        assert status_code == self.status_code, "Status code doesn't match expected {} found {}".format(self.status_code, status_code)
    
    def assert_response_contains(self, text):
        assert text in self.body, "Response body doesn't contains " + text
    
    def assert_response_header_contains(self, key, value):
        assert self.headers.get(key, None) == value, "Response headers doesn't contains {}:{}".format(
            key, value)


class PyJSON(object):
    def __init__(self, d):
        if type(d) is str:
            self.d = json.loads(d)
        else:
            self.d = self.from_dict(d)

    def from_dict(self, d):
        self.__dict__ = {}
        for key, value in d.items():
            if type(value) is dict:
                value = PyJSON(value)
            self.__dict__[key] = value

    def to_dict(self):
        d = {}
        for key, value in self.__dict__.items():
            if type(value) is PyJSON:
                value = value.to_dict()
            d[key] = value
        return d
    
    def get(self, key):
        if "." in key:
            tmp = self.d
            keys = key.split(".")
            for k in keys:
                tmp = tmp[k]
            return tmp
        else:
            return self.__dict__['d'][key]

    def __repr__(self):
        return str(self.to_dict())

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]
