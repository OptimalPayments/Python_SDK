'''
Created on 20-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from PythonNetBanxSDK.CardPayments.Authorization import Authorization
from PythonNetBanxSDK.CardPayments.Pagination import Pagination
from PythonNetBanxSDK.CardPayments.AuthorizationReversal import AuthorizationReversal
from PythonNetBanxSDK.CardPayments.Authentication import Authentication
from PythonNetBanxSDK.CardPayments.Verification import Verification
from PythonNetBanxSDK.CustomerVault.Profile import Profile
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

    def request_conflict_example_for_auth(self):
        '''
        Request Conflict Exception
        '''		
        auth_obj = Authorization(None)
        card_obj = Card(None)
        cardExpiry_obj = CardExpiry(None)
        billing_obj = BillingDetails(None)
        auth_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        auth_obj.amount("1")
        auth_obj.settleWithAuth("false")
        card_obj.cardNum("4917480000000008")
        card_obj.cvv("123")
        auth_obj.card(card_obj)
        cardExpiry_obj.month("12")
        cardExpiry_obj.year("2017")
        card_obj.cardExpiry(cardExpiry_obj)
        billing_obj.zip("M5H 2N2")
        auth_obj.billingDetails(billing_obj)
        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler().create_authorization(auth_obj)
        print ("Complete Response : ")
        print (response_object.__dict__)
        response_object = self._optimal_obj.card_payments_service_handler().create_authorization(auth_obj)
        print ("Complete Response : ")
        print (response_object.error.code)
        print (response_object.error.message)

	
    def create_authorization_with_payment_token(self):
        '''
        Create Authorization with payment token
        '''     
        auth_obj = Authorization(None)
        auth_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        auth_obj.amount("1200")
          
        card_obj = Card(None)
        card_obj.paymentToken("C7dEdq9Mcz4nwyy")
          
        auth_obj.card(card_obj)
        

        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).create_authorization(auth_obj)
                                            
        print ("Complete Response : ")
        print (response_object.__dict__)
        print ("Card ID: ", response_object.card.__dict__)


    def create_complex_authorization(self):
        '''
        Create Complex Authorization
        '''
        auth_obj = Authorization(None)
        authentication_obj = Authentication(None)
        card_obj = Card(None)
        cardExpiry_obj = CardExpiry(None)
        billing_obj = BillingDetails(None)
        shipping_obj = ShippingDetails(None)

        auth_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        auth_obj.amount("5")
        auth_obj.settleWithAuth("false")
        auth_obj.customerIp("204.91.0.12")

        card_obj.cardNum("5036150000001115")
        card_obj.cvv("123")
        auth_obj.card(card_obj)

        cardExpiry_obj.month("4")
        cardExpiry_obj.year("2017")
        card_obj.cardExpiry(cardExpiry_obj)

        authentication_obj.eci("5")
        authentication_obj.cavv("AAABCIEjYgAAAAAAlCNiENiWiV+=")
        authentication_obj.xid("OU9rcTRCY1VJTFlDWTFESXFtTHU=")
        authentication_obj.threeDEnrollment("Y")
        authentication_obj.threeDResult("Y")
        authentication_obj.signatureStatus("Y")
        auth_obj.authentication(authentication_obj)

        billing_obj.street("100 Queen Street West")
        billing_obj.city("Toronto")
        billing_obj.state("ON")
        billing_obj.country("CA")
        billing_obj.zip("M5H 2N2")
        auth_obj.billingDetails(billing_obj)

        shipping_obj.carrier("FEX")
        shipping_obj.shipMethod("C")
        shipping_obj.street("100 Queen Street West")
        shipping_obj.city("Toronto")
        shipping_obj.state("ON")
        shipping_obj.country("CA")
        shipping_obj.zip("M5H 2N2")
        auth_obj.shippingDetails(shipping_obj)
        
        #self.optimal_obj.card_payments_service_handler().lookup_authorization_with_id(auth_obj)

        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password,
                                             "TEST",
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).create_authorization(auth_obj)

        print ("Complete Response : ")
        print (response_object.__dict__)


    def create_authorization_with_card(self):
        '''
        Create Authorization with payment token
        '''     

        auth_obj = Authorization(None)
        card_obj = Card(None)
        cardExpiry_obj = CardExpiry(None)
        billing_obj = BillingDetails(None)
		
        auth_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        auth_obj.amount("1400")
        auth_obj.settleWithAuth("false")
		
        card_obj.cardNum("4530910000012345")
        card_obj.cvv("123")
        auth_obj.card(card_obj)
		
        cardExpiry_obj.month("2")
        cardExpiry_obj.year("2017")
        card_obj.cardExpiry(cardExpiry_obj)
		
        billing_obj.zip("M5H 2N2")
        auth_obj.billingDetails(billing_obj)
	

        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).create_authorization(auth_obj)
                                            
        print ("Complete Response : ")
        print (response_object.__dict__)
        print ("Card ID: ", response_object.card.__dict__)
		
    def payment_process_with_card_settle_with_auth_true(self):
        '''
        Process a card purchase (settleWithAuth=true)
        '''     

        auth_obj = Authorization(None)
        card_obj = Card(None)
        cardExpiry_obj = CardExpiry(None)
        billing_obj = BillingDetails(None)

        auth_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        auth_obj.amount("4")
        auth_obj.settleWithAuth("true")

        card_obj.cardNum("4530910000012345")
        card_obj.cvv("123")
        auth_obj.card(card_obj)

        cardExpiry_obj.month("2")
        cardExpiry_obj.year("2017")
        card_obj.cardExpiry(cardExpiry_obj)

        billing_obj.zip("M5H 2N2")
        auth_obj.billingDetails(billing_obj)

        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).create_authorization(auth_obj)

        print ("Complete Response : ")
        print (response_object.__dict__)
        print ("Card ID: ", response_object.card.__dict__)
        print("error code: ", response_object.error.code)
        print("error message: ", response_object.error.message)
        

    def partial_authorization_reversal(self):
        '''
        Partial authorization reversal
        '''
        auth_obj = Authorization(None)
        auth_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        auth_obj.amount(555)
        auth_obj.settleWithAuth("false")

        card_obj = Card(None)
        card_obj.cardNum("4530910000012345")
        card_obj.cvv("123")
        auth_obj.card(card_obj)

        cardExpiry_obj = CardExpiry(None)
        cardExpiry_obj.month("1")
        cardExpiry_obj.year("2017")
        card_obj.cardExpiry(cardExpiry_obj)

        billing_obj = BillingDetails(None)
        billing_obj.zip("M5H 2 N2")
        auth_obj.billingDetails(billing_obj)

        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).create_authorization(auth_obj)

        print ("Authorization Response : ", response_object.__dict__)
        auth_id = response_object.id
        print ("Authorization Id : ", auth_id)
        # dea6fd3a-3e47-4b44-a303-c5c38f7104f6
        auth_rev =  AuthorizationReversal(None)
        auth_rev.merchantRefNum(RandomTokenGenerator().generateToken())
        auth_rev.amount(222)

        auth_obj2 = Authorization(None)
        auth_obj2.id(auth_id)
        auth_rev.authorization(auth_obj2)

        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).reverse_authorization_using_merchant_no(auth_rev)

        print ("Complete Response : ")
        print (response_object.__dict__)

		
		
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
        pagination_obj = Pagination(None)
        #pagination_obj.limit = "4"
        #pagination_obj.offset = "0"
        #pagination_obj.startDate = "2015-02-10T06:08:56Z"
        #pagination_obj.endDate = "2015-02-20T06:08:56Z"
        #f0yxu8w57de4lris
        #zyp2pt3yi8p8ag9c
        auth_obj = Authorization(None)
        auth_obj.merchantRefNum("f0yxu8w57de4lris")
        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).lookup_authorization_with_merchant_no(auth_obj, pagination_obj)
        print ("Complete Response : ")
        print (response_object)
        #print (response_object.links[0].rel)
        #print (response_object.links[0].href)
        #print (response_object[0].links[0].href)
        print (response_object[0].__dict__)
        #print (response_object.error.fieldErrors[0].__dict__)
        #print (response_object.error.fieldErrors[1].__dict__)

            

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

    def verify_card_billing_details(self):
        '''
        Sample of verifying a card and billing details
        '''
        verify_obj = Verification(None)
        card_obj = Card(None)
        card_exp_obj = CardExpiry(None)
        billing_obj = BillingDetails(None)
        profile_obj = Profile(None)

        verify_obj.merchantRefNum("4lnvozq01d1pbkr0")
        #verify_obj.customerIp("204.91.0.12")
        #verify_obj.description("This is  a test transaction")

        #profile_obj.firstName("John")
        #profile_obj.lastName("Smith")
        #profile_obj.email("john.smith@somedomain.com")
        #verify_obj.profile(profile_obj)

        card_obj.cardNum("4530910000012345")
        card_obj.cvv("123")
        verify_obj.card(card_obj)

        card_exp_obj.month("02")
        card_exp_obj.year("2017")
        card_obj.cardExpiry(card_exp_obj)

        #billing_obj.street("100 Queen Street West")
        #billing_obj.city("Toronto")
        #billing_obj.state("ON")
        #billing_obj.country("CA")
        billing_obj.zip("M5H 2N2")
        verify_obj.billingDetails(billing_obj)

        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).verify_card(verify_obj)

        print ("Complete Response : ")
        print (response_object.__dict__)

    def verify_card_using_payment_token(self):
        '''
        Sample of verifying a card using payment token
        '''
        verify_obj = Verification(None)
        card_obj = Card(None)
        #card_exp_obj = CardExpiry(None)
        #billing_obj = BillingDetails(None)
        #profile_obj = Profile(None)
        #shipping_obj = ShippingDetails(None)

        verify_obj.merchantRefNum("rp12jb19igryjqff")
        card_obj.paymentToken("C7dEdq9Mcz4nwyy")
        #card_obj.cvv("123")
        verify_obj.card(card_obj)

        #shipping_obj.carrier("FEX")
        #shipping_obj.shipMethod("C")
        #shipping_obj.street("100 Queen Street West")
        #shipping_obj.city("Toronto")
        #shipping_obj.state("ON")
        #shipping_obj.country("CA")
        #shipping_obj.zip("M5H 2N2")
        #verify_obj.shippingDetails(shipping_obj)

        #card_exp_obj.month("09")
        #card_exp_obj.year("2019")
        #card_obj.cardExpiry(card_exp_obj)

        #billing_obj.street("100 Queen Street West")
        #billing_obj.city("Toronto")
        #billing_obj.state("ON")
        #billing_obj.country("CA")
        #billing_obj.zip("M5H 2N2")
        #verify_obj.billingDetails(billing_obj)

        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).verify_card(verify_obj)

        print ("Complete Response : ")
        print (response_object.__dict__)

    def lookup_verification_using_id(self):
        '''
        dd655ad9-2ebe-4178-9b3f-c88707a193f3
        '''
        verify_obj = Verification(None)
        verify_obj.id("dd655ad9-2ebe-4178-9b3f-c88707a193f3")

        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).lookup_verification_using_id(verify_obj)
                                            
        print ("Complete Response : ")
        print (response_object.__dict__)

    def lookup_verification_using_merchant_ref_num(self):
        '''
        4lnvozq01d1pbkr0
        '''
        pagination_obj = Pagination(None)
        pagination_obj.limit = "4"
        pagination_obj.offset = "0"
        #pagination_obj.startDate = "2015-02-10T06:08:56Z"
        #pagination_obj.endDate = "2015-02-20T06:08:56Z"
        
        verify_obj = Verification(None)
        verify_obj.merchantRefNum("4lnvozq01d1pbkr0")

        self._optimal_obj = OptimalApiClient(self._api_key,
                                             self._api_password, 
                                             "TEST", 
                                             self._account_number)
        response_object = self._optimal_obj.card_payments_service_handler(
                                            ).lookup_verification_using_merchant_ref_num(verify_obj, pagination_obj)
                                            
        print ("Complete Response : ")
        print (response_object)
        #print (response_object.links[0].rel)
        #print (response_object.links[0].href)
        #print (response_object[0].links[0].href)
        print (response_object[0].__dict__)
        #print (response_object.error.fieldErrors[0].__dict__)
        #print (response_object.error.fieldErrors[1].__dict__)
        
        for c in range(0, response_object.__len__()):
            print ('Records : ', c)
            print ('Verifications : ', response_object[c].__dict__)
        

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
o = SampleTest_Card().lookup_verification_using_merchant_ref_num()


        
        