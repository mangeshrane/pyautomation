import csv
import os
from pyautomation.file_manager.file_manager import FileManager
from pyautomation import LOG


class CSVReader(object):
    
    def __init__(self):
        pass
        
    @staticmethod
    def get_data_map(filename, header=None):
        with open(os.path.join(FileManager.get_test_datadir(), filename)) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=header)
            LOG.info("returning CSV data")
            return list(reader)