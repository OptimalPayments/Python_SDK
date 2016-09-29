'''
Created on 27-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK import common, HostedPayment
from PythonNetBanxSDK.common.DomainObject import DomainObject


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
    Property authType
    '''
    def authType(self, auth_type):
        self.__dict__['authType'] = auth_type
        
    '''
    Property confirmationNumber
    '''
    def confirmationNumber(self, confirmation_number):
        self.__dict__['confirmationNumber'] = confirmation_number
        
    '''
    Property currencyCode
    '''
    def currencyCode(self, currency_code):
        self.__dict__['currencyCode'] = currency_code
        
    '''
    Property mode
    '''
    def mode(self, mode):
        self.__dict__['mode'] = mode
        
    '''
    Property originalMerchantRefNum
    '''
    def originalMerchantRefNum(self, original_merchant_ref_num):
        self.__dict__['originalMerchantRefNum'] = original_merchant_ref_num
                    

    '''
    Property Id
    This is the order ID against which the refund has been requested.
    '''
    def id(self, id_):
        self.__dict__['id'] = id_

    '''
    Property Error
    @param: Error Object
    '''   
    def error(self, error):
        e = common.Error.Error(error)
        self.__dict__['error'] = e
