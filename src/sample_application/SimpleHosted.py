#!/usr/bin/env python3
'''
Created on 1-Apr-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from PythonNetBanxSDK.HostedPayment.Order import Order
from PythonNetBanxSDK.CustomerVault.Profile import Profile
from RandomTokenGenerator import RandomTokenGenerator
from Config import Config

optimal_obj = OptimalApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)

order_obj = Order(None)
order_obj.customerIp("14.140.42.67")
order_obj.merchantRefNum(str(RandomTokenGenerator().generateToken()))
order_obj.currencyCode("USD")
order_obj.totalAmount("1125")
order_obj.customerNotificationEmail("jane.smythe@emailhost.com")
             
profile_obj = Profile(None)
profile_obj.merchantCustomerId(str(RandomTokenGenerator().generateToken()))
profile_obj.firstName("Jane")
profile_obj.lastName("Smythe")             
order_obj.profile(profile_obj)

response_object = optimal_obj.hosted_payment_service_handler().create_order(order_obj)    

print ('Content-Type: text/html')
print ()
print ('<html>')
print ('<head><title>Hosted Payment - Create Order</title></head>')
print ('<body>')
print (response_object.__dict__)
print ('</body></html>')
