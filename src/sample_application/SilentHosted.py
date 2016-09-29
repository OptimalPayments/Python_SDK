#!/usr/bin/env python3
'''
Created on 1-Apr-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.CustomerVault.Profile import Profile
from PythonNetBanxSDK.HostedPayment.ExtendedOptions import ExtendedOptions
from PythonNetBanxSDK.HostedPayment.Order import Order
from PythonNetBanxSDK.HostedPayment.Redirect import Redirect
from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


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

eo_list = []
eo = ExtendedOptions(None)
eo.key("silentPost")
eo.value("true")
eo_list.append(eo.__dict__)
order_obj.extendedOptions(eo_list)
        
redirect_list = []
redirect1 = Redirect(None)
redirect1.rel("on_success")
redirect1.uri("https://api.netbanx.com/echo?payment=success")
        
redirect2 = Redirect(None)
redirect2.rel("on_error")
redirect2.uri("https://api.netbanx.com/echo?payment=error")
        
redirect3 = Redirect(None)
redirect3.rel("on_decline")
redirect3.uri("https://api.netbanx.com/echo?payment=failure")
        
redirect_list.append(redirect1.__dict__)
redirect_list.append(redirect2.__dict__)
redirect_list.append(redirect3.__dict__)
order_obj.redirect(redirect_list)

response_object = optimal_obj.hosted_payment_service_handler().create_order(order_obj) 

print ('Content-Type: text/html')
print ()
print ('<html>')
print ('<head><title>Hosted Payment - Silent Post</title></head>')
print ('<body>')
print (response_object.__dict__)
print ('</body></html>')
