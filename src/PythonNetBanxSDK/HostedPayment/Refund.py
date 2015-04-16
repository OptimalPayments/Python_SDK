'''
Created on 27-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.common.DomainObject import DomainObject
from PythonNetBanxSDK import common, HostedPayment


class Refund(DomainObject):
    '''
    classdocs
    '''


    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['order'] = self.order
        handler['error'] = self.error

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
    Property Merchant Reference Number
    '''   
    def merchantRefNum(self, merchant_ref_num):
        self.__dict__['merchantRefNum'] = merchant_ref_num

    '''
    Property Order
    @param: Order Object
    '''   
    def order(self, order):
        if isinstance(order, HostedPayment.Order.Order):
            self.__dict__['order'] = order
        else:
            o = HostedPayment.Order.Order(order)
            self.__dict__['order'] = o

    '''
    Property Error
    @param: Error Object
    '''   
    def error(self, error):
        e = common.Error.Error(error)
        self.__dict__['error'] = e
