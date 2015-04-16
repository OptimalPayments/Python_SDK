'''
Created on 25-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK import common
from PythonNetBanxSDK.common.DomainObject import DomainObject


class Card(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['brand'] = self.brand
        handler['country'] = self.country
        handler['expiry'] = self.expiry
        handler['lastDigits'] = self.lastDigits
        handler['threeDEnrolment'] = self.threeDEnrolment
        handler['type'] = self.type
        handler['error'] = self.error

        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property Brand
    '''   
    def brand(self, brand):
        self.__dict__['brand'] = brand
        
    '''
    Property Country
    '''   
    def country(self, country):
        self.__dict__['country'] = country
        
    '''
    Property Card Expiry
    '''   
    def expiry(self, expiry):
        self.__dict__['expiry'] = expiry
        
    '''
    Property Last Digits
    '''   
    def lastDigits(self, last_digits):
        self.__dict__['lastDigits'] = last_digits
        
    '''
    Property ThreeDEnrolment
    '''   
    def threeDEnrolment(self, three_denrollment):
        self.__dict__['threeDEnrolment'] = three_denrollment
        
    '''
    Property Type
    '''   
    def type(self, type_):
        self.__dict__['type'] = type_
        
    '''
    Property Error
    @param: Error Object
    '''   
    def error(self, error):
        e = common.Error.Error(error)
        self.__dict__['error'] = e
        