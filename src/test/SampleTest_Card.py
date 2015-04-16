'''
Created on 20-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from PythonNetBanxSDK.CardPayments.Authorization import Authorization
from PythonNetBanxSDK.CardPayments.Card import Card
from PythonNetBanxSDK.CardPayments.CardExpiry import CardExpiry
from PythonNetBanxSDK.CardPayments.BillingDetails import BillingDetails
from RandomTokenGenerator import RandomTokenGenerator
from PythonNetBanxSDK.CardPayments.ShippingDetails import ShippingDetails


class SampleTest_Card(object):
    '''
    classdocs
    '''

    # Static data
    _api_key = 'devcentre4628'
    _api_password = 'B-qa2-0-548ef25d-302b0213119f70d83213f828bc442dfd0af3280a7b48b1021400972746f9abe438554699c8fa3617063ca4c69a'
    _account_number = '89983472'


    def __init__(self):
        '''
        Constructor
        '''


    def card_payments_monitor(self):
        '''
        Card Payments Monitor
        '''
        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        #self._optimal_obj._update_env('www.google.co.in',10,30,30)
        response_object = self._optimal_obj.card_payments_service_handler().monitor()

        print ("response object : ")
        print (response_object.__dict__)  

        
    def create_authorization(self):
        '''
        Create Authorization with payment token
        '''     
        auth_obj = Authorization(None)
        auth_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        auth_obj.amount("1000")
          
        card_obj = Card(None)
        card_obj.paymentToken("Ca7aO2wuj6xxJVJ")
          
        auth_obj.card(card_obj)
        
		'''
		auth_obj = Authorization(None)
		card_obj = Card(None)
		cardExpiry = CardExpiry(None)
		billing_obj = BillingDetails(None)
		
		auth_obj.merchantRefNum(RandomTokenGenerator().generateToken())
		auth_obj.amount("4")
		auth_obj.settleWithAuth("True")
		
		card_obj.cardNum("4111111111111111")
        card_obj.cvv("123")
		auth_obj.card(card_obj)
		
		cardExpiry.month("2")
		cardExpiry.year("2017")
		card_obj.cardExpiry(cardExpiry_obj)
		
		billing_obj.zip("M5H 2N2")
		auth_obj.billingDetails(billing_obj)
		'''
		
#         auth_Obj = Authorization(None)
#         auth_Obj.merchantRefNum(RandomTokenGenerator().generateToken())
#         auth_Obj.amount("1031")
# 
#         card_obj = Card(None)
#         card_obj.cardNum("4510150000000321")
#         card_obj.type("VI")
#         card_obj.lastDigits("0321")  
#         card_obj.cvv("123")
#         cardExpiry_obj = CardExpiry(None)
#         print ("type of card expiry 1: ", type(cardExpiry_obj))
#         cardExpiry_obj.month("06")
#         cardExpiry_obj.year("2018")
#         print ("type of card expiry 2: ", type(cardExpiry_obj))
#         card_obj.cardExpiry(cardExpiry_obj)
#         print ("type of card expiry 3: ", type(cardExpiry_obj))  
#         auth_Obj.card(card_obj)
#         print ("type of card: ", type(card_obj))
#         print ("type of card expiry 4: ", type(cardExpiry_obj))
#         
#         billing_obj = BillingDetails(None)
#         billing_obj.zip("C1009ABK")
#         auth_Obj.billingDetails(billing_obj)

        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).create_authorization(auth_obj)
                                            
        print ("Complete Response : ")
        print (response_object.__dict__)
        print ("Card ID: ", response_object.card.__dict__)
        return (response_object.__dict__)
                             


    def lookup_authorization_with_id(self):
        '''
        Lookup Authorization with Id
        '''
        auth_obj = Authorization(None)
        auth_obj.id("5406f84a-c728-499e-b310-c55f4e52af9f")
        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).lookup_authorization_with_id(auth_obj)
        print ("Complete Response : ")
        print (response_object.__dict__)
                                   

            
            
    def lookup_authorization_with_merchant_ref_num(self):
        '''
        Lookup Authorization with Id
        '''
        auth_obj = Authorization(None)
        auth_obj.merchantRefNum("zyp2pt3yi8p8ag9c")
        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).lookup_authorization_with_merchant_no(auth_obj)
        print ("Complete Response : ")
        for c in range(0, response_object.__len__()):
            print (response_object[c].__dict__)
                                            

            

    def complete_authorization(self):
        '''
        Complete
        '''
        auth_obj = Authorization(None)
        auth_obj.id("55b77870-266c-4796-bce1-008334aad424")
        auth_obj.status("COMPLETED")
        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).complete_authorization_request(auth_obj)
                                            
        print ("Complete Response : ")
        print (response_object.__dict__)
                                            


    def settle_authorization(self):
        '''
        Settle an Authorization
        '''
        auth_obj = Authorization(None)
        auth_obj.id("55b77870-266c-4796-bce1-008334aad424")
        auth_obj.merchantRefNum("5m8652wc1pirizft")
        auth_obj.amount("500")
        #auth_obj.dupCheck(True)
        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).settle_authorization(auth_obj)
                                            
        print ("Complete Response : ")
        print (response_object.__dict__)
                                            

    def create_transaction_test(self):
        '''
        Sample of complete transaction request
        '''
        billing_obj = BillingDetails(None)
        shipping_obj = ShippingDetails(None)
        auth_obj = Authorization(None)
        card_obj = Card(None)
        card_exp_obj = CardExpiry(None)
        
        billing_obj.street("Carlos Pellegrini 551")
        billing_obj.city("Buenos Aires")
        billing_obj.state("CA")
        billing_obj.country("US")
        billing_obj.zip("M5H 2N2")
        
        shipping_obj.carrier("CAD")
        shipping_obj.city("Buenos Aires")
        shipping_obj.state("ON")
        shipping_obj.country("CA")
        shipping_obj.zip("M5H 2N2")
        
        card_obj.cardNum("5191330000004415")
        card_exp_obj.month("09")
        card_exp_obj.year("2019")
        card_obj.cardExpiry(card_exp_obj)
        
        auth_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        auth_obj.amount("1200")
        auth_obj.settleWithAuth(True)
        auth_obj.dupCheck(True)
        auth_obj.card(card_obj)
        auth_obj.billingDetails(billing_obj)
        auth_obj.shippingDetails(shipping_obj)
        
        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).create_authorization(auth_obj)
                                            
        print ("Complete Response : ")
        print (response_object.__dict__)        



# Call Object
o = SampleTest_Card().card_payments_monitor()


        
        