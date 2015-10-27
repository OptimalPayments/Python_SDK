'''
Created on 23-Feb-2015

@author: asawari.vaidya
'''

import random
import string

class RandomTokenGenerator(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def generateToken(self):
        token = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(16))
        return (token)