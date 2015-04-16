'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.common.DomainObject import DomainObject


class AssociatedTransactions(DomainObject):
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
        handler['authType'] = self.authType
        handler['dateTime'] = self.dateTime
        handler['reference'] = self.reference
        
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
    Property Auth Type
    '''   
    def authType(self, auth_type):
        self.__dict__['authType'] = auth_type
        
    '''
    Property Date Time
    '''   
    def dateTime(self, date_time):
        self.__dict__['dateTime'] = date_time
        
    '''
    Property Reference
    '''   
    def reference(self, reference):
        self.__dict__['reference'] = reference

