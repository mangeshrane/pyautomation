import xlrd
import os
from pyautomation.file_manager.file_manager import FileManager
from pyautomation.logger.logger import LOG


class ExcelReader(object):
    
    def __init__(self):
        pass
        
    @staticmethod    
    def get_data_map(filename, data_filter, sheet_no=0):
        workbook = xlrd.open_workbook(os.path.join(FileManager.get_test_datadir(), filename))
        LOG.info("using excel sheet " + filename)
        data_filter = data_filter
        sheet = workbook.sheet_by_index(sheet_no)
        
        flag = False
        for row in range(sheet.nrows):
            if sheet.cell(row, 0).value == data_filter:
                s_index = row + 1
                flag = True
            elif flag and sheet.cell(row, 0).value == "END":
                e_index = row
                flag = False
                
        keys = [sheet.cell(s_index, col_index).value for col_index in range(sheet.ncols)]

        dict_list = []
        for row_index in range(s_index + 1, e_index):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value 
                 for col_index in range(sheet.ncols)}
            d = {key: d[key] for key in [key for key in d.keys() if key ]}
            dict_list.append(d)
        LOG.info("returning data from excel")
        return dict_list   
    
    @staticmethod
    def get_data(filename, data_filter, sheet_no=0, fields=None):
        dataset = ExcelReader.get_data_map(filename, data_filter, sheet_no)
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

