# coding: UTF-8
'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from RandomTokenGenerator import RandomTokenGenerator 
from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from PythonNetBanxSDK.CustomerVault.Profile import Profile
from PythonNetBanxSDK.CustomerVault.Addresses import Address
from PythonNetBanxSDK.CustomerVault.DateOfBirth import DateOfBirth
from PythonNetBanxSDK.CustomerVault.Card import Card
from PythonNetBanxSDK.common.CardExpiry import CardExpiry
from PythonNetBanxSDK import common
import urllib3
from urllib3.connectionpool import HTTPSConnectionPool
import json
import certifi


class SampleTest_Customer(object):
    '''
    classdocs
    '''

    # Static data
    _api_key1 = 'devcentre4628'
    _api_password1 = 'B-qa2-0-548ef25d-302b0213119f70d83213f828bc442dfd0af3280a7b48b1021400972746f9abe438554699c8fa3617063ca4c69a'
    _account_number1 = '89983472'

    #_api_key = 'opus-sbox'
    #_api_password = 'B-qa2-0-54c80abb-0-302d0215008374329e4db71b82151c15f3be823700c155372602142a2afa9979ec90b59e2232dd292ee1798aa1f5b2'
    #_account_number = '1001187820'
    
    _api_key = 'devcentre4651'
    _api_password = 'B-qa2-0-54b5374e-302d02147911306b5c6db4ad74e083803733163195c75ef902150095b4a21a5ea7f4c19b7b37aed1944490b59e785e'
    _account_number = '1000032987'


    optimal_obj = OptimalApiClient(_api_key,
                                   _api_password,
                                    "TEST",
                                    _account_number)
    
    optimal_obj1 = OptimalApiClient(_api_key1,
                                   _api_password1,
                                    "TEST",
                                    _account_number1)
    
    def __init__(self):
        '''
        Constructor
        '''
 
    def customer_vault_monitor(self):
        '''
        Customer Vault Monitor
        '''
        response_object = self.optimal_obj.customer_vault_service_handler(
                                            ).monitor()
        
        print ("response object : ")
        print (response_object.status)        
                
    def create_customer_profile(self):      
        '''
        Create Customer Profile
        '''        
        profile_obj = Profile(None)
        #profile_obj.merchantCustomerId("4jdccmrtcqb964u1")
        profile_obj.merchantCustomerId(RandomTokenGenerator().generateToken())
        profile_obj.locale("en_US")
        profile_obj.firstName("Andr\u00E9 Jean")
        profile_obj.lastName("Smith")
        profile_obj.email("john.smith@somedomain.com")
        profile_obj.phone("713-444-5555")
        
        print ("api-key======", self.optimal_obj1._api_key)
        print ("api-password======", self.optimal_obj1._api_password)
        print ("api-account======", self.optimal_obj1._account_number)
        
        response_object = self.optimal_obj1.customer_vault_service_handler(
                                            ).create_profile(profile_obj)
        
        print ("response object : ")
        print (response_object.__dict__)
        print (response_object.error.__dict__)		
            
            
    '''
    lookup Customer Profile
    '''
    def lookup_customer_profile(self):
        profile_obj = Profile(None)
        #profile_obj.id("d1ecd379-58d3-4850-abce-744efb1eea91")
        #profile_obj.id("f7db7ffe-87ab-4df9-8f04-0d405128473f")
        #profile_obj.id("f920d2a3-6582-4cc2-acc6-bdf7cfa626a3")
		#f25a445d-395d-43dd-bd8d-f82cbe46dd40 - android
		#1df156a3-d977-409a-9a4a-3bfb405e88a7
        profile_obj.id("1df156a3-d977-409a-9a4a-3bfb405e88a7")
     
        response_object = self.optimal_obj.customer_vault_service_handler().lookup_profile(profile_obj)
        print ("response object : ")
        print (response_object.__dict__)
        print (response_object)
        if isinstance(response_object.error, common.Error.Error):
            print (response_object.error.code)
            print (response_object.error.message)
        else:
            print (response_object.id)
        

    
    
    def lookup_customer_profile_subcomponents(self):
        '''
        lookup Customer Profile Subcomponents
        '''
        is_addresses = True
        is_cards = True
        profile_obj = Profile(None)
		#dae5f3d7-aa7c-45c0-8d41-23fc82022f6a - singleusetoken
        #profile_obj.id("f920d2a3-6582-4cc2-acc6-bdf7cfa626a3")
        #d76208a7-cc28-4803-bbf3-e2091f124824
        profile_obj.id("4818c6de-5687-4afb-930d-cbeb106bf757")
		
        response_object = self.optimal_obj1.customer_vault_service_handler(
                                            ).lookup_profile_subcomponents(
                                            profile_obj, 
                                            is_addresses, 
                                            is_cards)

        print ("Response : ")
        print (response_object.__dict__)
        #print ("Addresses:")
        #for c in range(0, response_object.addresses.__len__()):
        #    print (response_object.addresses[c].id)
        print ("Cards:")
        
        for c in range(0, response_object.cards.__len__()):
            print (response_object.cards[c].__dict__)
            print (response_object.cards[c].id)
            print (response_object.cards[c].cardExpiry.month)
            print (response_object.cards[c].paymentToken)
        

    
            
    def update_customer_profile(self):
        '''
        Update Customer Profile
        mycustomer11765
        6ce868cf-5488-414c-87a1-d51dc461a3e2
 
        '''        
        profile_obj = Profile(None)
        profile_obj.id("e5f567a2-6661-45ef-8103-48069c51c6a2")
        profile_obj.merchantCustomerId("4y7t56kdls6u25yh")
        profile_obj.locale("en_US")
        profile_obj.firstName("John")
        profile_obj.middleName("Wilbur")
        profile_obj.lastName("")
        profile_obj.gender("M")
        profile_obj.email("")
        dob = DateOfBirth(None)
        dob.day("27")
        dob.month("12")
        dob.year("1990")
            
        profile_obj.dateOfBirth(dob)
        print ("date of birth=====", profile_obj.dateOfBirth.day)  
        
        print ("request object:", profile_obj.__dict__)

        response_object = self.optimal_obj.customer_vault_service_handler(
                                            ).update_profile(profile_obj)
                  
        print ("Response: ==========")
        print (response_object)                          


    def delete_customer_profile(self):
        '''
        Delete Customer Profile
        '''
        profile_obj = Profile(None)
        profile_obj.id("71e7f7a6-0849-40fc-989f-31ffe1460d89")
         
        response_object = self.optimal_obj.customer_vault_service_handler(
                                                ).delete_profile(profile_obj)
    
        print ("Respone Object : ")
        print (response_object)            


    def create_address(self):
        '''
        Create Customer Address
        '''
        address_obj = Address(None)
#         address_obj.country("AR")
#         address_obj.city("Buenos Aires")
#         address_obj.street("Carlos Pellegrini 551")
#         address_obj.street2("1009 Buenos Aires")
#         address_obj.zip("C1009ABK")

        address_obj.nickName("home")
        address_obj.street("100 Queen Street West")
        address_obj.street2("Unit 201")
        address_obj.city("Toronto")
        address_obj.country("CA")
        address_obj.state("ON")
        address_obj.zip("M5H 2N2")
        address_obj.phone("647-788-3901")
        address_obj.recipientName("Jane Doe")
            
        profile_obj = Profile(None)
        profile_obj.id("556ab258-cacc-406c-8cd8-412fde6b6e4f")
        address_obj.profile(profile_obj)
    
        response_object = self.optimal_obj.customer_vault_service_handler(
                                            ).create_address(address_obj)
    
        print ("Respone Object : ")
        print (response_object.__dict__)    



    def lookup_address(self):
        '''
        lookup Customer Address
        '''
        address_obj = Address(None)
        address_obj.id("7fc8a442-88c9-45d1-a480-88d45a532816")
          
        profile_obj = Profile(None)
        profile_obj.id("f920d2a3-6582-4cc2-acc6-bdf7cfa626a3")
        address_obj.profile(profile_obj)

        response_object = self.optimal_obj.customer_vault_service_handler(
                                            ).lookup_address(address_obj)
                                            
        print ("Respone Object : ")
        print (response_object.__dict__)  
        if isinstance(response_object.error, common.Error.Error):
            print (response_object.error.code)
            print (response_object.error.message)
        else:
            print (response_object.id)

    
    
    def update_address(self):
        '''
        Update Customer Address
        '''
        address_obj = Address(None)
        address_obj.id("f6bb6f41-962b-4cb3-8011-53cc7be60d29")
        address_obj.country("CA")
        address_obj.city("Toronto")
        address_obj.nickName("home")
        address_obj.street("323 Queen Street West")
        address_obj.state("ON")
        address_obj.zip("M5H 2N2")
        address_obj.recipientName("Jane Doe")
        address_obj.phone("647-788-3901")
            
        profile_obj = Profile(None)
        profile_obj.id("f920d2a3-6582-4cc2-acc6-bdf7cfa626a3")
        address_obj.profile(profile_obj)

        response_object = self.optimal_obj.customer_vault_service_handler(
                                            ).update_address(address_obj)
        print ("Respone Object : ")
        print (response_object.__dict__)  



    def delete_address(self):
        '''
        Delete Customer Address
        '''
        address_obj = Address(None)
        address_obj.id("0f668bb8-67c2-46a7-919b-e6de289b4a08")
          
        profile_obj = Profile(None)
        profile_obj.id("f920d2a3-6582-4cc2-acc6-bdf7cfa626a3")
        address_obj.profile(profile_obj)
  
        response_object = self.optimal_obj.customer_vault_service_handler(
                                            ).delete_address(address_obj)
        print ("Respone Object : ")
        print (response_object.__dict__)  
   


    def create_card(self):
        '''
        Create Customer Card
        '''
        card_obj = Card(None)
        card_obj.nickName("John's corporate Visa")
        card_obj.holderName("MR. JOHN SMITH")
        #6759950000000162
		#4917480000000008
		#4530910000012345
        #375529360131002
        card_obj.cardNum("375529360131002")
        card_obj.billingAddressId("0c84d4a4-97f2-4cbd-b92b-3a7c9403b69e")
        card_obj.defaultCardIndicator("true")
        card_exp_obj = CardExpiry(None)
        card_exp_obj.month("12")
        card_exp_obj.year("2019")
        profile_obj = Profile(None)
        #rofile_obj.id("f25a445d-395d-43dd-bd8d-f82cbe46dd40")
        profile_obj.id("34361085-c873-4b2f-a61e-18cfdc5bd02c")
        card_obj.profile(profile_obj)
        card_obj.cardExpiry(card_exp_obj)

        response_object = self.optimal_obj.customer_vault_service_handler(
                                            ).create_card(card_obj)

        print ("Response Values : ")
        print (response_object.__dict__)



    def lookup_card(self):
        '''
        Lookup Customer Card
        '''
        card_obj = Card(None)
        card_obj.id("492d583b-4360-4cae-affe-1d7fc8cb3a7b")
                
        profile_obj = Profile(None)
        profile_obj.id("f920d2a3-6582-4cc2-acc6-bdf7cfa626a3")
        card_obj.profile(profile_obj)

        response_object = self.optimal_obj.customer_vault_service_handler(
                                            ).lookup_card(card_obj)
        print ("Respone Object : ")
        print (response_object.__dict__)  
            
            
    def update_card(self):
        '''
        Update Customer Card
        '''
        card_obj = Card(None)
        card_obj.id("177fa616-0375-4b09-865b-a6d570eb415a")
        card_obj.holderName("MR. JOHN JAMES SMITH")
        card_obj.defaultCardIndicator("false")
        card_exp_obj = CardExpiry(None)
        card_exp_obj.month("12")
        card_exp_obj.year("2019")
                
        profile_obj = Profile(None)
        profile_obj.id("34361085-c873-4b2f-a61e-18cfdc5bd02c")
        card_obj.profile(profile_obj)
        card_obj.cardExpiry(card_exp_obj)

        response_object = self.optimal_obj.customer_vault_service_handler(
                                            ).update_card(card_obj)
        print ("Respone Object : ")
        print (response_object.__dict__)  
            

    def delete_card(self):
        '''
        Delete Customer Card
        '''
        card_obj = Card(None)
        card_obj.id("86824a20-4076-47f9-88fc-c24b0dc2bd51")
          
        profile_obj = Profile(None)
        profile_obj.id("f920d2a3-6582-4cc2-acc6-bdf7cfa626a3")
        card_obj.profile(profile_obj)

        response_object = self.optimal_obj.customer_vault_service_handler(
                                            ).delete_card(card_obj)
        print ("Respone Object : ")
        print (response_object.__dict__)

        
    def create_profile_single_use_token_2(self):
        data = {
            "card": {
                "holderName": "MR. JOHN SMITH",
                "cardNum": "4917484589897107",
                "cardExpiry": {
                    "month": "12",
                    "year": "2019"
                },
                "billingAddress": {
                    "street": "100 Queen Street West",
                    "street2": "Unit 201",
                    "city": "Toronto",
                    "country": "CA",
                    "state": "ON",
                    "zip": "M5H 2N2"
                }
            }
        }

        #username = 'devcentre4651'
        #password = 'B-qa2-0-54b5374e-302d02147911306b5c6db4ad74e083803733163195c75ef902150095b4a21a5ea7f4c19b7b37aed1944490b59e785e'
        url = "/customervault/v1/singleusetokens"    
        
        header_content = {"content-type": "application/json;charset=utf-8"}
        header_auth = {"Authorization": "Basic T1QtMTYxNTY6Qi1xYTItMC01NTJiOWJjZi0wLTMwMmMwMjE0NGVkOGY5YjhhZWE5ZDY1YjQ0Yjc3YTE2YTgxZWM1ZjlhYjkxNmY4YzAyMTQyYjRlNjliM2EyNzJiODY2YjFlMjYzYjBiMGM3YTkyNWE4OTQ1NDE4"}
        #auth_header = urllib3.util.make_headers(basic_auth=username+":"+password)
        
        pool = HTTPSConnectionPool('api.test.netbanx.com',
                                    cert_reqs='CERT_REQUIRED',
                                    ca_certs=certifi.where())
        pool.headers.update(header_content)
        pool.headers.update(header_auth)
        
        response = pool.urlopen("POST", url, body=json.dumps(data))
        
        print (response.status)
        print (response.data)
        
        res = response.data
        resp_str = res.decode('utf-8')
        json_obj = json.loads(resp_str)
        
        print ("payment token", json_obj['paymentToken'])        
        
        return (json_obj['paymentToken'])
        

    def create_profile_single_use_token(self):
        '''
        Create Profile using Single Use Token
        '''
             
        profile_obj1 = Profile(None)
        profile_obj1.merchantCustomerId(RandomTokenGenerator().generateToken())
        profile_obj1.locale("en_US")
        #profile_obj.firstName("John")
        #profile_obj.lastName("Smith")
        #profile_obj.email("john.smith@somedomain.com")
        #profile_obj.phone("713-444-5555")
        
        card_obj = Card(None)
        #card_obj.singleUseToken("SCO0Jpx9JUP9hESh")
        card_obj.singleUseToken(self.create_profile_single_use_token_2())
        profile_obj1.card(card_obj)
        print ("api-key======", self.optimal_obj._api_key)
        print ("api-password======", self.optimal_obj._api_password)
        print ("api-account======", self.optimal_obj._account_number)
        #print ("api-key======", self.optimal_obj._api_key)
        
        response_object = self.optimal_obj.customer_vault_service_handler(
                                ).create_profile(profile_obj1)
        print ("Respone Object : ")
        print (response_object.__dict__)  
        print (response_object.error.code)
        print (response_object.error.message)
        


o = SampleTest_Customer().create_customer_profile()
