'''
Created on Mar 19, 2019

@author: mrane
'''
import requests
from requests import Session
import urllib.parse
import json
from requests.auth import HTTPDigestAuth
from pprint import pformat
from pyautomation.api.response import Response
from pyautomation.configuration import CONFIG
import allure
from pyautomation.commons.helpers import expand_escape_sequence
from pyautomation.logger.logger import LOG


class Request(object):
    '''
    Wrapper around requests library whoch makes building requests and response Validation easier
    '''

    def __init__(self):

        self._headers = {}
        self._body = None
        self._cookies = {}
        self._params = {}
        self._path_param = {}
        self._base_url = None
        self.stream = False
        self._timeout = CONFIG.get("api.request.timeout", None)
        self._cert_file = False
        self._json_data = None
        self._session = Session()
        self._method = ""
        self._proxy = None
        self._files = None
        self._auth = None

    def header(self, Accept):
        if type(Accept).__name__ == 'dict':
            self._headers.update(Accept)

        else:
            raise ValueError
        return self

    def add_header(self, key, value):
        self._headers[key] = value

    def add_headers(self, header_dict):
        if isinstance(header_dict, dict):
            self._headers.update(header_dict)
        else:
            LOG.error('Parameter must be of dictionary type')
            raise ValueError("Parameter must be of dictionary type")
        return self

    def cookie(self, key, value):
        self._cookies[key] = value
        return self
    
    def add_param(self, key, value):
        if key in self._params:
            if isinstance(self._params[key], list):
                self._params[key].append(value)
            else:
                self._params[key] = [self._params[key], value]
        else:
            self._params[key] = value
        return self

    def set_base_url(self, url):
        self._base_url = url
        return self
    
    def set_path_param(self, key, value):
        self._path_param[key] = value
        return self
    
    def set_path_params(self, params_dict):
        if isinstance(params_dict, dict):
            for key, value in params_dict.items():
                self.set_path_param(key, value)
        else:
            LOG.error('Path params should be specified in dictionary')
            raise ValueError("Path params should be specified in dictionary")
    
    def add_form_params(self, param_dict):
        if isinstance(param_dict, dict):
            for key, val in param_dict.items():
                self.add_param(key, val)
        else:
            LOG.error('Form params should be specified in dictionary')
            raise ValueError("Form params should be specified in dictionary ")
        return self

    def set_body(self, body, file=False):
        if file:
            self._body = {'file': open(body, 'rb')}
        else:
            self._body = body
        return self

    def raw_reponse(self):
        self.stream = True
        return self

    def relax_ssl_validation(self):
        self._cert_file = False
        return self

    def set_timeout(self, timeout):
        self._timeout = timeout
        return self

    def set_cert_file(self, path):
        self._cert_file = path
        return self

    def set_json_body(self, json_data):
        self._json_data = json.loads(json_data)
        return self

    def _build_request(self, method, endpoint=""):
        if endpoint:
            self._base_url = urllib.parse.urljoin(self._base_url, endpoint)
        if self._path_param:
            self._base_url = self._base_url.format(**self._path_param)
        self._request = requests.Request(method, self._base_url,
                                         headers=self._headers, 
                                         files=self._files,
                                         data=self._body, 
                                         json=self._json_data,
                                         auth=self._auth,
                                         params=self._params)
        self._request = self._request.prepare()

    def _get_resp(self):
        LOG.info("API Request : " + expand_escape_sequence(str({k: v for k, v in self._request.__dict__.items()})))
        allure.attach('<p>{0}<p>'.format(expand_escape_sequence(pformat(str({k: v for k, v in self._request.__dict__.items()})))),
                      "Request",
                      allure.attachment_type.HTML)
        return Response(self._session.send(self._request,
                                           stream=self.stream,
                                           verify=self._cert_file,
                                           proxies=self._proxy,
                                           cert=self._cert_file,
                                           timeout=self._timeout
                                           ))

    def get(self, endpoint=''):
        self._build_request('GET', endpoint)
        return self._get_resp()

    def post(self, endpoint=''):
        self._build_request('POST', endpoint)
        return self._get_resp()
    
    def put(self, endpoint=""):
        self._build_request("PUT", endpoint)
        return self._get_resp()
    
    def delete(self, endpoint=""):
        self._build_request("DELETE", endpoint)
        return self._get_resp()
    
    def head(self, endpoint=""):
        self._build_request("HEAD", endpoint)
        return self._get_resp()
    
    def auth(self, username, password, atype="basic"):
        if atype == "basic":
            self._auth = (username, password)
        elif atype == "digest":
            self._auth = HTTPDigestAuth('user', 'pass')
        return self

class ContentType:
    JSON = {'Content-Type': 'application/json'}
    XML = {'Content-Type': "application/xml"}
    HTML = {'Content-Type': "text/html"}
    TEXT = {'Content-Type': 'text/plain'}
    URLENC = {'Content-Type': 'application/x-www-form-urlencoded'}
    BINARY = {'Content-Type': 'application/octet-stream'}


class Accept:
    XMl = {'Accept': 'application/xml'}
    JSON = {'Accept': 'application/json'}
