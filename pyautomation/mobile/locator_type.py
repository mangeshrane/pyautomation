'''
Created on Apr 15, 2019

@author: mrane
'''
class UiAutomator:
    
    def __init__(self):
        self.locator = "new UiSelector()"
    
    def resourceid(self, idx):
        self.locator += '.resourceId("{0}")'.format(idx) 
        return self
    
    def class_name(self, name):
        self.locator += '.className("{0}")'.format(name)
        return self
    
    def text(self, text):
        self.locator += '.text("{0}")'.format(text)
        return self
    
    def partial_text(self, text):
        self.locator += '.textContains("{0}")'.format(text)
        return self
    
    def index(self, index):
        self.locator += '.index("{0}")'.format(index)
        return self
    
    def clickable(self, clickable):
        self.locator += '.clickable("{0}")'.format(clickable)
        return self
    
    def checked(self, checked):
        self.locator += '.checked("{0}")'.format(checked)
        return self
    
    def enabled(self, enabled):
        self.locator += '.enabled("{0}")'.format(enabled)
        return self
    
    def description(self, desc):
        self.locator += '.description("{0}")'.format(desc)
        return self
    
    def partial_description(self, desc):
        self.locator += '.descriptionContains("{0}")'.format(desc)
        return self
