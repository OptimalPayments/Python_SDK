'''
Created on 19-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK import HostedPayment
from PythonNetBanxSDK.HostedPayment.Card import Card
from PythonNetBanxSDK.common.DomainObject import DomainObject


class Transaction(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['associatedTransactions'] = self.associatedTransactions
        handler['card'] = self.card
        handler['errorCode'] = self.errorCode
        handler['errorMessage'] = self.errorMessage
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
                
    '''
    Property Status
    '''   
    def status(self, status):
        self.__dict__['status'] = status
    
    '''
    Property Last Update
    '''   
    def lastUpdate(self, last_update):
        self.__dict__['lastUpdate'] = last_update
        
    '''
    Property Auth Type
    '''   
    def authType(self, auth_type):
        self.__dict__['authType'] = auth_type
    
    '''
    Property Auth Code
    '''   
    def authCode(self, auth_code):
        self.__dict__['authCode'] = auth_code
        
    '''
    Property Merchant Reference Number
    '''   
    def merchantRefNum(self, merchant_ref_num):
        self.__dict__['merchantRefNum'] = merchant_ref_num
        
    '''
    Property Associated Transactions
    @param: AssociatedTransactions Object
    '''   
    def associatedTransactions(self, associated_transactions):
        if isinstance(
                associated_transactions, 
                HostedPayment.AssociatedTransactions.AssociatedTransactions):
            at = HostedPayment.AssociatedTransactions.AssociatedTransactions(
                                            associated_transactions.__dict__)
            self.__dict__['associatedTransactions'] = at
        else:  
            for count in range(0, associated_transactions.__len__()):  
                at = HostedPayment.AssociatedTransactions.AssociatedTransactions(
                                            associated_transactions[count])
                self.__dict__.setdefault('associatedTransactions',[]).append(at)
        
    '''
    Property Card
    @param: Card Object
    '''   
    def card(self, card):
        if isinstance(card, Card):
            c = Card(card.__dict__)
            self.__dict__['card'] = c
        else:
            c = Card(card)
            self.__dict__['card'] = c
        
    '''
    Property Confirmation Number
    '''   
    def confirmationNumber(self, confirmation_number):
        self.__dict__['confirmationNumber'] = confirmation_number
        
    '''
    Property Currency Code
    '''   
    def currencyCode(self, currency_code):
        self.__dict__['currencyCode'] = currency_code
        
    '''
    Property Amount
    '''   
    def amount(self, amount):
        self.__dict__['amount'] = amount
        
    '''
    Property Payment Type
    '''   
    def paymentType(self, payment_type):
        self.__dict__['paymentType'] = payment_type
        
    '''
    Property Settled
    '''   
    def settled(self, settled):
        self.__dict__['settled'] = settled
        
    '''
    Property Refunded
    '''   
    def refunded(self, refunded):
        self.__dict__['refunded'] = refunded
        
    '''
    Property Reversed
    '''   
    def reversed(self, reversed_):
        self.__dict__['reversed'] = reversed_
        
    '''
    Property Date Time
    '''   
    def dateTime(self, date_time):
        self.__dict__['dateTime'] = date_time
        
    '''
    Property Cvd Verification
    '''   
    def cvdVerification(self, cvd_verification):
        self.__dict__['cvdVerification'] = cvd_verification
        
    '''
    Property House Number Verification
    '''   
    def houseNumberVerification(self, house_number_verification):
        self.__dict__['houseNumberVerification'] = house_number_verification
        
    '''
    Property Zip Verification
    '''   
    def zipVerification(self, zip_verification):
        self.__dict__['zipVerification'] = zip_verification
        
    '''
    Property Risk Reason Code
    '''   
    def riskReasonCode(self, risk_reason_code):
        self.__dict__['riskReasonCode'] = risk_reason_code
        
    '''
    Property Error Code
    '''   
    def errorCode(self, error_code):
        self.__dict__['errorCode'] = error_code
        
    '''
    Property Error Message
    '''   
    def errorMessage(self, error_message):
        self.__dict__['errorMessage'] = error_message
