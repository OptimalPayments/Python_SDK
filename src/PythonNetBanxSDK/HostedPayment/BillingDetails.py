'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.common.DomainObject import DomainObject


class BillingDetails(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['city'] = self.city
        handler['country'] = self.country
        handler['street'] = self.street
        handler['street2'] = self.street2
        handler['zip'] = self.zip
        handler['state'] = self.state
        handler['phone'] = self.phone
        handler['useAsShippingAddress'] = self.useAsShippingAddress
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property City
    '''   
    def city(self, city):
        self.__dict__['city'] = city
        
    '''
    Property Country
    '''   
    def country(self, country):
        self.__dict__['country'] = country
        
    '''
    Property Street
    '''   
    def street(self, street):
        self.__dict__['street'] = street
        
    '''
    Property Street2
    '''   
    def street2(self, street2):
        self.__dict['street2'] = street2
        
    '''
    Property Zip
    '''   
    def zip(self, zip_):
        self.__dict__['zip'] = zip_
        
    '''
    Property State
    '''   
    def state(self, state):
        self.__dict__['state'] = state
        
    '''
    Property Phone
    '''   
    def phone(self, phone):
        self.__dict__['phone'] = phone
    
    '''
    Property Use As Shipping Address
    '''   
    def useAsShippingAddress(self, use_as_shipping_address):
        self.__dict__['useAsShippingAddress'] = use_as_shipping_address
