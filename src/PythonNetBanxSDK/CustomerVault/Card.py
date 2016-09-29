'''
Created on 24-Feb-2015

@author: asawari.vaidya
'''
from PythonNetBanxSDK import CustomerVault
from PythonNetBanxSDK import common
from PythonNetBanxSDK.common.CardExpiry import CardExpiry
from PythonNetBanxSDK.common.DomainObject import DomainObject
from PythonNetBanxSDK.CustomerVault.Addresses import Address
from PythonNetBanxSDK.common.Link import Link


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
        handler['cardExpiry'] = self.cardExpiry      
        handler['profile'] = self.profile
        handler['error'] = self.error
        handler['links'] = self.links
        handler['billingAddress'] = self.billingAddress
        
        
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
    Property Single Use Token
    '''
    def singleUseToken(self, single_use_token):
        self.__dict__['singleUseToken'] = single_use_token

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
    Property Holder Name
    '''        
    def holderName(self, holder_name):
        self.__dict__['holderName'] = holder_name

    '''
    Property Card Number
    '''        
    def cardNum(self, card_num):
        self.__dict__['cardNum'] = card_num
        
    '''
    Property Card Bin
    '''        
    def cardBin(self, card_bin):
        self.__dict__['cardBin'] = card_bin
        
    '''
    Property Last Digits
    '''        
    def lastDigits(self, last_digits):
        self.__dict__['lastDigits'] = last_digits
        
    '''
    Property Card Expiry
    @param: CardExpiry Object
    '''        
    def cardExpiry(self, card_expiry):
        if isinstance (card_expiry, CardExpiry):
            ce = CardExpiry(card_expiry.__dict__)
            self.__dict__['cardExpiry'] = ce.__dict__
        else:
            ce = CardExpiry(card_expiry)
            self.__dict__['cardExpiry'] = ce
            
    '''
    Property Card Type
    '''        
    def cardType(self, card_type):
        self.__dict__['cardType'] = card_type
    
    '''
    Property Billing Address
    '''
    def billingAddress(self, billing_address):
        if isinstance (billing_address, Address):
            p = Address(billing_address.__dict__)
            self.__dict__['billingAddress'] = p.__dict__
        else:
            p = Address(billing_address)
            self.__dict__['billingAddress'] = p
    
    '''
    Property Billing Address Id
    '''        
    def billingAddressId(self, billing_address_id):
        self.__dict__['billingAddressId'] = billing_address_id
        
    '''
    Property Default Card Indicator
    '''        
    def defaultCardIndicator(self, default_card_indicator):
        self.__dict__['defaultCardIndicator'] = default_card_indicator
                            
    '''
    Property Payment Token
    '''        
    def paymentToken(self, payment_token):
        self.__dict__['paymentToken'] = payment_token
        
    '''
    Property Profile
    @param: Profile Object
    '''        
    def profile(self, profile):
        p = CustomerVault.Profile.Profile(profile.__dict__)
        self.__dict__['profile'] = p
    
    '''
    Property Error
    @param: Error Object
    '''        
    def error(self, error):
        e = common.Error.Error(error)
        self.__dict__['error'] = e
    
    '''
    Property Status
    '''        
    def status(self, status):
        self.__dict__['status'] = status
        
    '''
    Property Links
    @param: Link Object, List of Link objects
    '''        
    def links(self, links):
        if isinstance(links, Link):
            l = Link(links)
            self.__dict__['links'] = l
        else:
            for count in range(0, links.__len__()):
                l = Link(links[count])
                self.__dict__.setdefault('links', []).append(l)
  
