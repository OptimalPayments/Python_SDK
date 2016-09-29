'''
Created on 01-Apr-2016

@author: Murali.Mohan
'''
from PythonNetBanxSDK import CustomerVault
from PythonNetBanxSDK.CustomerVault.Mandates import Mandates
from PythonNetBanxSDK.common.DomainObject import DomainObject
from PythonNetBanxSDK.common.Error import Error


class SEPABankAccount(DomainObject):

    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['profile'] = self.profile
        handler['mandates'] = self.mandates
        handler['error'] = self.error
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
            
    '''
    Property Id
    '''        
    def id(self, id_):
        self.__dict__['id'] = id_
        
    '''
    Property Nick Name
    '''
    def nickName(self, nick_name):
        self.__dict__['nickName'] = nick_name
        
    '''
    Property Merchant Reference Number
    '''
    def merchantRefNum(self, merchant_ref_num):
        self.__dict__['merchantRefNum'] = merchant_ref_num
        
    '''
    Property Status
    '''
    def status(self, status):
        self.__dict__['status'] = status
        
    '''
    Propert Status Reason
    '''
    def statusReason(self, status_reason):
        self.__dict__['statusReason'] = status_reason
        
    '''
    Property iban
    '''
    def iban(self, iban):
        self.__dict__['iban'] = iban
    
    '''
    Property Mandate Reference
    '''
    def mandateReference(self, mandate_reference):
        self.__dict__['mandateReference'] = mandate_reference
    
    '''
    Property bic
    '''
    def bic(self, bic):
        self.__dict__['bic'] = bic
        
    '''
    Property Account Holder Name
    '''
    def accountHolderName(self, account_holder_name):
        self.__dict__['accountHolderName'] = account_holder_name
        
    '''
    Property Last Digits
    '''
    def lastDigits(self, last_digits):
        self.__dict__['lastDigits'] = last_digits
        
    '''
    Property Billing Address Id
    '''
    def billingAddressId(self, billing_address_id):
        self.__dict__['billingAddressId'] = billing_address_id
        
    '''
    Property Payment Token
    '''
    def paymentToken(self, payment_token):
        self.__dict__['paymentToken'] = payment_token
        
    '''
    Property Mandates
    '''
    def mandates(self, mandates):
        for count in range(0, mandates.__len__()):
            mandate_obj = Mandates(mandates[count])
            self.__dict__.setdefault('mandates', []).append(mandate_obj)
        
    '''
    Property Error
    @param: Error Object
    '''        
    def error(self, error):
        e = Error(error)
        self.__dict__['error'] = e

    '''
    Property Profile
    @param: Profile Object
    '''        
    def profile(self, profile):
        p = CustomerVault.Profile.Profile(profile.__dict__)
        self.__dict__['profile'] = p