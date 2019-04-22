import csv
import os
from core.file_manager.file_manager import FileManager
from core.logger import LOG


class CSVReader():
    
    @staticmethod
    def get_data(filename, fields, headers=None):
        with open(os.path.join(FileManager.get_test_datadir(), filename)) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=headers)
            LOG.info("returning CSV data")
            dataset = list(reader)
        if headers:
            dataset = dataset[1:]
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