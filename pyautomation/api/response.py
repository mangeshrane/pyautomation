'''
Created on Mar 20, 2019

@author: mrane
'''
import json

from requests.models import Response as rp
from collections import namedtuple
from pprint import pformat
import allure
from pyautomation.logger.logger import LOG
from jsonschema.validators import validate
from jsonschema.exceptions import ValidationError

ALLURE_RESP_TML = '<p> <h> <b> URL: </b> </h> {0}</p><p> <h> <b> Body<br> </b> </h> {1}</p><p> <h> <b> Headers<br> </b> </h> {2}</p><p> <h> <b> cookies<br> </b> </h> {3}</p><p> <h> <b> Status Code<br> </b> </h> {4}</p>'


class Response(object):
    '''
    classdocs
    '''

    def __init__(self, response):
        '''
        Constructor
        '''
        LOG.info("API Response body : " + str(response.text))
        LOG.info("API Response headers : " + str(response.headers))
        LOG.info("API Response cookies : " + str(response.cookies))
        LOG.info("API Response status code : " + str(response.status_code))
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

    def _json_object_hook(self, d):
        return namedtuple('response', d.keys())(*d.values())

    def json2obj(self, data):
        return json.loads(data, object_hook=self._json_object_hook)
    
    def validate_schema(self, schema):
        try:
            validate(instance=self.body, schema=schema)
        except ValidationError as e:
            LOG.error("Schema Validation error occured :" + e.message)
            return False
        else:
            return True
    
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
