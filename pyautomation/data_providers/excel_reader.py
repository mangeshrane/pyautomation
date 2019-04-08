import xlrd
import os
from pyautomation.file_manager.file_manager import FileManager
from pyautomation import LOG


class ExcelReader(object):
    
    def __init__(self):
        pass
        
    @staticmethod    
    def get_data_map(filename, data_filter, headers=True, sheet_no=0):
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
