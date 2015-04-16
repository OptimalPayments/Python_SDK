#!/usr/bin/python3

'''
Created on 1-Apr-2015

@author: Asawari.Vaidya
'''
#import sys
#sys.path.append('../.')
from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from PythonNetBanxSDK.CustomerVault.Profile import Profile
from RandomTokenGenerator import RandomTokenGenerator
from Config import Config

optimal_obj = OptimalApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)

profile_obj = Profile(None)
profile_obj.merchantCustomerId(RandomTokenGenerator().generateToken())
profile_obj.locale("en_US")
profile_obj.firstName("John")
profile_obj.lastName("Smith")
profile_obj.email("john.@smith@somedomain.com")
profile_obj.phone("713-444-5555")
           
response_object = optimal_obj.customer_vault_service_handler().create_profile(profile_obj)

print ('Content-Type: text/html')
print ()
print ('<html>')
print ('<head><title>Customer Vault - Create Customer Profile</title></head>')
print ('<body>')
print (response_object.__dict__)
Print ('</body></html>')
