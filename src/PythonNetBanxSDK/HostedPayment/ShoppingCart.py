'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.common.DomainObject import DomainObject


class ShoppingCart(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['amount'] = self.amount
        handler['description'] = self.description
        handler['sku'] = self.sku
        handler['quantity'] = self.quantity
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:

            pass
        
    '''
    Property Amount
    '''   
    def amount(self, amount):
        self.__dict__['amount'] = amount
    
    '''
    Property Description
    '''   
    def description(self, description):
        self.__dict__['description'] = description
        
    '''
    Property Sku
    '''   
    def sku(self, sku):
        self.__dict__['sku'] = sku
        
    '''
    Property Quantity
    '''   
    def quantity(self, quantity):
        self.__dict__['quantity'] = quantity
    