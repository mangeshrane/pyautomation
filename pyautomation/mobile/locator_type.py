'''
Created on Apr 15, 2019

@author: mrane
'''
class UiSelector:
    '''
    UISelector builder for finding element using find_element_by_android_uiautomator
    
    Usage:
        driver.find_element_by_android_uiautomator(UiAutomator().checked("true").class_name("com.android.widget"))
        
    '''
    def __init__(self):
        self.locator = "new UiSelector()"
    
    def resourceid(self, idx):
        self.locator += '.resourceId("{0}")'.format(idx) 
        return self
    
    def class_name(self, name):
        self.locator += '.className("{0}")'.format(name)
        return self
    
    def class_name_matches(self, regex):
        self.locator += '.classNameMatches({0})'.format(regex)
        
    def description_matches(self, regex):
        self.locator += '.descriptionMatches("{0}")'.format(regex)
        return self
    
    def description_starts_with(self, desc):
        self.locator += '.descriptionStartsWith("{0}")'.format(desc)
        return self
    
    def focusable(self, val):
        self.locator += '.focusable({0})'.format(val)
        return self
    
    def focused(self, val):
        self.locator += '.focused({0})'.format(val)
        return self
    
    def instance(self, instance_no):
        self.locator += '.instance({})'.format(instance_no)
        return self
        
    def long_clickable(self, val):
        self.locator += '.longClickable({})'.format(val)
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
    
    def checkable(self, value):
        self.locator += '.checkable({0})'.format(value)
        return self
    
    def child_selector(self, UiSelector):
        self.locator += '.childSelector({0})'.format(UiSelector)
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
    
    def package_name(self, name):
        self.locator += '.packageName("{}")'.format(name)
        return self
    
    def package_name_matches(self, regex):
        self.locator += '.packageNameMatches("{0}")'.format(regex)
        return self
    
    def resourceid_matches(self, regex):
        self.locator += '.resourceIdMatches("{}")'.format(regex)
        return self
    
    def scrollable(self, val):
        self.locator += '.scrollable({})'.format(val)
        return self
    
    def selected(self, val):
        self.locator += '.selected({})'.format(val)
        return self
    
    def text_matches(self, regex):
        self.locator += '.textMatches("{}")'.format(regex)
        return self
    
    def text_starts_with(self, text):
        self.locator += 'textStartsWith("{}")'.format(text)
        return self
    