#!/usr/bin/env python3
'''
Created on 1-June-2016

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.CustomerVault.Addresses import Address
from PythonNetBanxSDK.CustomerVault.Profile import Profile
from PythonNetBanxSDK.CustomerVault.SEPABankAccount import SEPABankAccount
from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from utils.Utils import Utils

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


optimal_obj = OptimalApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)

# Create Customer Profile
profile_obj = Profile(None)
profile_obj.merchantCustomerId(RandomTokenGenerator().generateToken())
profile_obj.locale("en_US")
profile_obj.firstName("John")
profile_obj.lastName("Smith")
profile_obj.email("john.smith@somedomain.com")
profile_obj.phone("713-444-5555")
        
response_object = optimal_obj.customer_vault_service_handler().create_profile(profile_obj)

# Create Address
address_obj = Address(None)
address_obj.nickName("home")
address_obj.street("100 Queen Street West")
address_obj.street2("Unit 201")
address_obj.city("Toronto")
address_obj.country("CA")
address_obj.state("ON")
address_obj.zip("M5H 2N2")
address_obj.phone("647-788-3901")
address_obj.recipientName("Jane Doe")
            
profile_obj1 = Profile(None)
profile_obj1.id(response_object.id)
address_obj.profile(profile_obj1)
    
response_object2 = optimal_obj.customer_vault_service_handler().create_address(address_obj)

# Create SEPA Bank Account
sepabankaccount_obj = SEPABankAccount(None)
sepabankaccount_obj.nickName("Sally's Account")
sepabankaccount_obj.accountHolderName("Sally Barnes")
sepabankaccount_obj.iban("LB30099900000001001925579115")
sepabankaccount_obj.bic("ABNANL2A")
sepabankaccount_obj.billingAddressId(response_object2.id)
    
profile_obj2 = Profile(None)
profile_obj2.id(response_object.id)
    
sepabankaccount_obj.profile(profile_obj2)
response_object3 = optimal_obj.customer_vault_service_handler().create_sepa_bank_account(sepabankaccount_obj)

print ('\nProfile Id : ', response_object.id)
print ('\nAddress Id : ', response_object2.id)
print ("\nResponse Values ==========> ")
Utils.print_response(response_object3)

