'''
Created on May 7, 2019

@author: mrane
'''
from PyPDF2 import PdfFileReader

class PdfReader(object):

    def __init__(self, filename):
        '''
        Constructor
        '''
        with open(filename, 'rb') as f:
            self.pdf = PdfFileReader(f)
            self.info = self.pdf.getDocumentInfo()
            self._number_of_pages = self.pdf.getNumPages()
    
    @property
    def number_of_pages(self):
        return self._number_of_pages
        
