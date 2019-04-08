
import pprint
from pyautomation.data_providers.csv_reader import CSVReader
from pyautomation.data_providers.excel_reader import ExcelReader
from pyautomation.data_providers.json_reader import JSONReader

def get_data(filename, data_filter="", fields=None, headers=True):
    if str(filename).endswith("csv"):
        dataset = CSVReader.get_data_map(filename)
        print()
        if headers:
            dataset = dataset[1:]
    elif str(filename).endswith("xls") or str(filename).endswith("xlsx"):
        dataset = ExcelReader.get_data_map(filename, data_filter, headers)
    elif str(filename).endswith("json"):
        dataset = JSONReader.get_data_map(filename)
    else:
        raise UnsupportedFileFormat("Datafile must be csv, xls or json")
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


class UnsupportedFileFormat(Exception):
    pass

pprint.pprint(get_data("users.csv"))
