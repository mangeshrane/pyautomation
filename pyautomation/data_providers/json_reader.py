import json
from collections import namedtuple
from builtins import staticmethod
import os

from pyautomation.file_manager.file_manager import FileManager
from pyautomation.logger.logger import LOG

class JSONReader(object):

    @staticmethod
    def get_data_map(filename):
        with open(os.path.join(FileManager.get_test_datadir(), filename)) as f:
            raw = f.read()
        j = json.loads(raw)
        LOG.info("returning data from json file : " + filename)
        return j

    @staticmethod
    def json2obj(name, data):
        return json.loads(data, object_hook=lambda d: namedtuple(name, d.keys())(*d.values()))
    
    @staticmethod
    def get_data(filename, fields=None):
        dataset = JSONReader.get_data_map(filename)
        edata = []
        if fields:
            for data in dataset:
                edata.append(
                    tuple(data[f] for f in fields)
                    )
            data = (",".join(fields), edata)
            return data
        else:
            for data in dataset:
                keys = list(dataset[0].keys())
                edata.append(tuple(data[f] for f in keys))
            data = (",".join(keys), edata)
            return data