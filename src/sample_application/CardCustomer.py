#!/usr/bin/python3
'''
Created on 1-Apr-2015

@author: Asawari.Vaidya
'''
import cgitb
cgitb.enable()
import cgi
from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from PythonNetBanxSDK.CardPayments.Authorization import Authorization
from PythonNetBanxSDK.CardPayments.Card import Card
from PythonNetBanxSDK.CardPayments.CardExpiry import CardExpiry
from RandomTokenGenerator import RandomTokenGenerator
from Config import Config

form = cgi.FieldStorage()
payment_token = form.getvalue('paymentToken')

optimal_obj = OptimalApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)

auth_obj = Authorization(None)
card_obj = Card(None)
auth_obj.merchantRefNum(RandomTokenGenerator().generateToken())
auth_obj.amount("2006")
card_obj.paymentToken(payment_token)
auth_obj.card(card_obj)


response_object = optimal_obj.card_payments_service_handler().create_authorization(auth_obj)    

print ('Content-Type: text/html')
print ()
print ('<html>')
print ('<head><title>Card Payments - Create  Authorization with Payment Token</title></head>')
print ('<body>')
print (response_object.__dict__)
print ('</body></html>')
