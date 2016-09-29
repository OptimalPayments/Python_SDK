#!/usr/bin/env python3
'''
Created on 1-June-2016

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.CardPayments.BillingDetails import BillingDetails
from PythonNetBanxSDK.CustomerVault.EFTBankAccount import EFTBankAccount
from PythonNetBanxSDK.CustomerVault.Profile import Profile
from PythonNetBanxSDK.DirectDebit.Purchase import Purchase
from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from utils.Utils import Utils

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


optimal_obj = OptimalApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number_EFT)
purchase_obj = Purchase(None)
purchase_obj.merchantRefNum(RandomTokenGenerator().generateToken())
purchase_obj.amount("10098")
purchase_obj.customerIp("192.0.126.111")

eftbank_obj = EFTBankAccount(None)
eftbank_obj.accountHolderName("XYZ Company")
eftbank_obj.accountNumber("336657")
eftbank_obj.transitNumber("22446")
eftbank_obj.institutionId("001")

profile_obj = Profile(None)
profile_obj.firstName("Joe")
profile_obj.lastName("Smith")
profile_obj.email("Joe.Smith@hotmail.com")

billingdetails_obj = BillingDetails(None)
billingdetails_obj.street("100 Queen Street West")
billingdetails_obj.city("Ottawa")
billingdetails_obj.state("ON")
billingdetails_obj.country("CA")
billingdetails_obj.zip("M1M1M1")
billingdetails_obj.phone("6139991100")

purchase_obj.profile(profile_obj)
purchase_obj.billingDetails(billingdetails_obj)
purchase_obj.eft(eftbank_obj)

response_object = optimal_obj.direct_debit_service_handler().submit_purchase(purchase_obj)

print ("\nResponse Values ==========> ")
Utils.print_response(response_object)

