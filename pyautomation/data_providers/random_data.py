'''
Created on Feb 11, 2019

@author: mrane
'''
import random
import string


class Random(object):
    '''
    This class generates random test data
    '''

    @staticmethod
    def get_random_string(length=10):
        """
        returns string of alpha-numeric characters with default length 10
        """
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

    @staticmethod
    def get_random_characters(length=10):
        """
        Returns only alpha string
        """
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

    @staticmethod
    def get_random_digits(length=10):
        """
        returns a numeric string 
        """
        return ''.join(random.choice(string.digits) for _ in range(length))
