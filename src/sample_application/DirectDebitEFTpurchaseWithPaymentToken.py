#!/usr/bin/env python3
'''
Created on 1-June-2016

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.CustomerVault.EFTBankAccount import EFTBankAccount
from PythonNetBanxSDK.DirectDebit.Purchase import Purchase
from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from utils.Utils import Utils

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


optimal_obj = OptimalApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number_EFT)
purchase_obj = Purchase(None)
purchase_obj.merchantRefNum(RandomTokenGenerator().generateToken())
purchase_obj.amount("10098")

eftbank_obj = EFTBankAccount(None)
eftbank_obj.paymentToken("Dw6TqO65OiBamTA")
purchase_obj.eft(eftbank_obj)

response_object = optimal_obj.direct_debit_service_handler().submit_purchase(purchase_obj)

print ("\nResponse Values ==========> ")
Utils.print_response(response_object)

