'''
Created on Jan 24, 2019

'''
import os
import re


class FileManager(object):
    '''
    File Manager:
    
    This class contains methods to manage files
     
    '''
    __rootdir__ = ""
    TEST_DATA = ""
    
    @classmethod
    def get_test_datadir(cls):
        """
            returns TEST_DATA directory for project
        """
        cls.TEST_DATA = os.path.join(cls.get_project_root(), "testdata")
        return cls.TEST_DATA
    
    @staticmethod
    def create_folder_structure(folders_string):
        """
        Creates folder structure specified in a string
        """
        os.makedirs(folders_string)
        
    @classmethod
    def get_project_root(cls):
        """
        returns a project root directory which is identified by '.rootfile'
        root directory can be changed by moving '.rootfile'
        """
        if(cls.__rootdir__):
            return cls.__rootdir__

        path = os.getcwd()
        seperator_matches = re.finditer("/|\\\\", path)

        paths_to_search = [path]
        for match in seperator_matches:
            p = path[:match.start()]
            paths_to_search.insert(0, p)

        for path in paths_to_search:
            target_path = os.path.join(path, ".rootfile")
            if os.path.isfile(target_path):
                cls.__root_folder__ = path
                return cls.__root_folder__
