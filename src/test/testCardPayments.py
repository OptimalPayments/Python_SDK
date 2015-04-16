from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from PythonNetBanxSDK.CustomerVault.Profile import Profile
from PythonNetBanxSDK.CustomerVault.Addresses import Address
from PythonNetBanxSDK.CardPayments.Card import Card
from PythonNetBanxSDK.CardPayments.CardExpiry import CardExpiry
from PythonNetBanxSDK.CardPayments.BillingDetails import BillingDetails
from PythonNetBanxSDK.CardPayments.Authorization import Authorization
from PythonNetBanxSDK.CardPayments.Settlement import Settlement
from PythonNetBanxSDK.CardPayments.Refund import Refund
from PythonNetBanxSDK.CardPayments.AuthorizationReversal import AuthorizationReversal
from PythonNetBanxSDK.common.DomainObject import DomainObject
from PythonNetBanxSDK.CardPayments.ShippingDetails import ShippingDetails
from test.RandomTokenGenerator import RandomTokenGenerator


api_key = 'devcentre4628'
api_password = 'B-qa2-0-548ef25d-302b0213119f70d83213f828bc442dfd0af3280a7b48b1021400972746f9abe438554699c8fa3617063ca4c69a'
account_number = '89983472'

optimalApiCli = OptimalApiClient(api_key,api_password, "TEST", account_number)

tokenGenerator = RandomTokenGenerator()

def printDictionary(dictObj,tabSpace):
    for key in dictObj:
        if (isinstance(dictObj[key],dict)):
            printDictionary(dictObj[key],(tabSpace + "  "))
        else:
            print(tabSpace, "     ", key, " = ", dictObj[key])

def preetyPrint(resObj, tabSpace):
    print(tabSpace,type(resObj),"[")
    for key in resObj.__dict__.keys():
        #print("Resolving key ", key, " ===========>")
        if (isinstance(resObj.__dict__[key],DomainObject)):
            preetyPrint(resObj.__dict__[key],(tabSpace + "  "))
        elif (isinstance(resObj.__dict__[key],dict)):
            printDictionary(resObj.__dict__[key],(tabSpace + "  "))
        elif (isinstance(resObj.__dict__[key],list)):
            for c in range(0, resObj.__dict__[key].__len__()):
                if (isinstance(resObj.__dict__[key][c],dict)):
                    printDictionary(resObj.__dict__[key][c],(tabSpace + "  "))
                elif (isinstance(resObj.__dict__[key][c],list)):
                    for cnt in range(0, resObj.__dict__[key][c].__len__()):
                        preetyPrint(resObj.__dict__[key][c][cnt],(tabSpace + "  "))
                else:
                    print(tabSpace, "     ", key, " = ", resObj.__dict__[key][c])
        else:
            print(tabSpace, "     ", key, " = ", resObj.__dict__[key])
    print(tabSpace,"]")

def pprint(resObj, tabSpace):
    if(isinstance(resObj, list)):
        for c in range(0,resObj.__len__()):
            print("====================== Data-",(c+1)," ======================")
            preetyPrint(resObj[c],"")
            print("====================== Data-",(c+1)," Ends ======================")
    else:
        preetyPrint(resObj,"")
    
merchantRefNo=tokenGenerator.generateToken()#"mycustomer0192005"
amount="1009"
    
def testPurchaseRequest():
    
    auth_Obj = Authorization(None)
    auth_Obj.merchantRefNum(merchantRefNo)#last was 43
    auth_Obj.amount(amount)
    auth_Obj.settleWithAuth(True)
    cardExpiry_obj = CardExpiry(None)
    cardExpiry_obj.month("06")
    cardExpiry_obj.year("2018")
    card_obj = Card(None)
    card_obj.cardNum("4510150000000321")
    card_obj.type("VI")
    card_obj.lastDigits("0321")
    card_obj.cardExpiry(cardExpiry_obj)
    card_obj.cvv("123")
    billingDetails_obj = BillingDetails(None)
    billingDetails_obj.zip("411028")
    auth_Obj.billingDetails(billingDetails_obj)
    auth_Obj.card(card_obj)
    response_object = optimalApiCli.card_payments_service_handler().create_authorization(auth_Obj)
    print("Purchase request completed with following response: ")
    preetyPrint(response_object,"")

def testLookUpAuthById():
    auth_Obj = Authorization(None)
    auth_Obj.id("b85d1850-51c8-4868-9c16-92e3b28d0760")
    auth_resp = optimalApiCli.card_payments_service_handler().lookup_authorization_with_id(auth_Obj)
    print("Authorization available with following response: ")
    preetyPrint(auth_resp,"")
    
def testReverseAuthorization():
    auth_Obj = Authorization(None)
    auth_Obj.id("5406f84a-c728-499e-b310-c55f4e52af9f")
    auth_resp = optimalApiCli.card_payments_service_handler().lookup_authorization_with_id(auth_Obj)
    print("Authorization available with following response: ")
    preetyPrint(auth_resp,"")
    
    #auth_Obj = Authorization(None)
    #auth_Obj.merchantRefNum(merchantRefNo)#last was 43
    #auth_Obj.amount(amount)
    #auth_Obj.settleWithAuth(False)
    #cardExpiry_obj = CardExpiry(None)
    #cardExpiry_obj.month("06")
    #cardExpiry_obj.year("2018")
    #card_obj = Card(None)
    #card_obj.cardNum("4510150000000321")
    #card_obj.type("VI")
    #card_obj.lastDigits("0321")
    #card_obj.cardExpiry(cardExpiry_obj)
    #card_obj.cvv("123")
    #billingDetails_obj = BillingDetails(None)
    #billingDetails_obj.zip("411028")
    #auth_Obj.billingDetails(billingDetails_obj)
    #auth_Obj.card(card_obj)
    #auth_resp = optimalApiCli.card_payments_service_handler().create_authorization(auth_Obj)
    #print("Purchase request completed with following response: ")
    #preetyPrint(auth_resp,"")
    
    
    auh_rev_obj = AuthorizationReversal(None)
    auh_rev_obj.merchantRefNum(str(auth_resp.merchantRefNum))
    auh_rev_obj.authorization(auth_resp)
    
    print(optimalApiCli.to_dictionary(auh_rev_obj))
    
    response_object = optimalApiCli.card_payments_service_handler().reverse_authorization_using_merchant_no(auh_rev_obj)
    print("Authorization reversal request completed with following response: ")
    preetyPrint(response_object,"")

def testAuthorizationByPaymentToken():
    #get the profile
    profile_Obj = Profile(None)
    profile_Obj.id("93d2f486-a61b-43d3-b718-d974354f244d")
    
    prof_resp_object = optimalApiCli.customer_vault_service_handler().lookup_profile(profile_Obj)
    print("Profile available with id: ", prof_resp_object.id)
    preetyPrint(prof_resp_object,"")
    
    #get the card
    card_obj = Card(None)
    card_obj.id("7262db7c-7750-4a25-963f-a5fe11999713")
    card_obj.profile(prof_resp_object)
    card_resp_obj = optimalApiCli.customer_vault_service_handler().lookup_card(card_obj)
    print("Card availabe with following response: ")
    preetyPrint(card_resp_obj,"")
    
    #get the address for shipping address detail
    address_Obj2 = Address(None)
    address_Obj2.id("acfd8c44-d76b-45ad-92a0-e8298aba7636")
    address_Obj2.profile(prof_resp_object)
    ship_add_resp_obj = optimalApiCli.customer_vault_service_handler().lookup_address(address_Obj2)
    print("Shipping address availabe with following response: ")
    preetyPrint(ship_add_resp_obj,"")
    
    
    shippingDetails_obj = ShippingDetails(None)
    shippingDetails_obj.carrier("UPS")
    shippingDetails_obj.shipMethod("N")
    shippingDetails_obj.street(ship_add_resp_obj.street)
    shippingDetails_obj.city(ship_add_resp_obj.city)
    shippingDetails_obj.state(ship_add_resp_obj.state)
    shippingDetails_obj.country(ship_add_resp_obj.country)
    shippingDetails_obj.zip("411028")
    
    
    auth_Obj = Authorization(None)
    auth_Obj.merchantRefNum("5oc1n2jx54oqpgm0")
    #auth_Obj.merchantRefNum(merchantRefNo)
    auth_Obj.amount(amount)
    auth_Obj.settleWithAuth(False)
    card_obj = Card(None)
    card_obj.paymentToken(card_resp_obj.paymentToken)
    #card_obj.paymentToken("Cr7ovhT9LAcfroZ")
    auth_Obj.card(card_obj)
    auth_Obj.shippingDetails(shippingDetails_obj)
    
    auth_Obj.customerIp("14.140.42.67")
    auth_Obj.description("Test Authoization on card by paymenttoken")
    response_object = optimalApiCli.card_payments_service_handler().create_authorization(auth_Obj)
    print("Authorization with payment token completed with following response: ")
    preetyPrint(response_object,"")
    #print(optimalApiCli.to_dictionary(auth_Obj))


def testLookupAuthByMerchantRefNo():
    #get the auth by id
    auth_Obj = Authorization(None)
    auth_Obj.id("1fb8bc4f-cfb6-46ad-92c3-b8a460ce6534")
    auth_resp = optimalApiCli.card_payments_service_handler().lookup_authorization_with_id(auth_Obj)
    
    
    auth_Obj2 = Authorization(None)
    #auth_Obj2.merchantRefNum("5oc1n2jx54oqpgm1")
    auth_Obj2.merchantRefNum(auth_resp.merchantRefNum)
    auth_resp2 = optimalApiCli.card_payments_service_handler().lookup_authorization_with_merchant_no(auth_Obj2)
    print("Authorization available by merchant ref no. with following response: ")
    pprint(auth_resp2,"")
    
def testCreateHeldAuthUsingCard():
    #get the profile
    profile_Obj = Profile(None)
    profile_Obj.id("93d2f486-a61b-43d3-b718-d974354f244d")
    
    prof_resp_object = optimalApiCli.customer_vault_service_handler().lookup_profile(profile_Obj)
    print("Profile available with id: ", prof_resp_object.id)
    preetyPrint(prof_resp_object,"")
    
    #get the card
    card_obj = Card(None)
    card_obj.id("2ed7de4f-5be9-44cd-8b32-2b2e3015aacd")
    card_obj.profile(prof_resp_object)
    card_resp_obj = optimalApiCli.customer_vault_service_handler().lookup_card(card_obj)
    #print("Card availabe with Cardnumber:" + card_resp_obj.cardNum +" retrieved with following response: ")
    print("Card availabe with following response: ")
    preetyPrint(card_resp_obj,"")
    
    #get the address for shipping address detail
    address_Obj2 = Address(None)
    address_Obj2.id("acfd8c44-d76b-45ad-92a0-e8298aba7636")
    address_Obj2.profile(prof_resp_object)
    ship_add_resp_obj = optimalApiCli.customer_vault_service_handler().lookup_address(address_Obj2)
    print("Shipping address availabe with following response: ")
    preetyPrint(ship_add_resp_obj,"")
    
    shippingDetails_obj = ShippingDetails(None)
    shippingDetails_obj.carrier("UPS")
    shippingDetails_obj.shipMethod("N")
    shippingDetails_obj.street(ship_add_resp_obj.street)
    shippingDetails_obj.city(ship_add_resp_obj.city)
    shippingDetails_obj.state(ship_add_resp_obj.state)
    shippingDetails_obj.country(ship_add_resp_obj.country)
    shippingDetails_obj.zip("411028")
    
    billingDetails_obj = BillingDetails(None)
    billingDetails_obj.country("AR")
    billingDetails_obj.zip("C1009ABK")
    
    auth_Obj = Authorization(None)
    #auth_Obj.merchantRefNum("5oc1n2jx54oqpgm0")
    auth_Obj.merchantRefNum(merchantRefNo)
    auth_Obj.amount(amount)
    auth_Obj.settleWithAuth(False)
    
    cardExpiry_obj = CardExpiry(None)
    cardExpiry_obj.month(card_resp_obj.cardExpiry.month)
    cardExpiry_obj.year(card_resp_obj.cardExpiry.year)
    card_obj = Card(None)
    card_obj.cardNum("4510150000000321")
    card_obj.type(card_resp_obj.cardType)
    card_obj.lastDigits(card_resp_obj.lastDigits)
    card_obj.cardExpiry(cardExpiry_obj)
    auth_Obj.card(card_obj)
    
    auth_Obj.shippingDetails(shippingDetails_obj)
    auth_Obj.billingDetails(billingDetails_obj)
    auth_Obj.customerIp("14.140.42.67")
    auth_Obj.description("Test Authoization on card by paymenttoken")
    response_object = optimalApiCli.card_payments_service_handler().create_authorization(auth_Obj)
    print("Authorization with payment token completed with following response: ")
    preetyPrint(response_object,"")

def testCancelHeldAuthorization():
    auth_Obj2 = Authorization(None)
    auth_Obj2.id("b85d1850-51c8-4868-9c16-92e3b28d0760")
    auth_Obj2.status("CANCELLED")
    auth_resp2 = optimalApiCli.card_payments_service_handler().cancel_held_authorization(auth_Obj2)
    print("Held Authorization cancelled with following response: ")
    preetyPrint(auth_resp2,"")
    
def testLookupAuthReversalById():
    auh_rev_obj = AuthorizationReversal(None)
    auh_rev_obj.id("e652cbe3-bc90-41bf-9291-be1ff9a5571d")
    
    response_object = optimalApiCli.card_payments_service_handler().lookup_authorization_reversal_with_id(auh_rev_obj)
    print("Authorization reversal available with following response: ")
    preetyPrint(response_object,"")

def testLookupAuthRevByMerchantRefNo():
    auh_rev_obj = AuthorizationReversal(None)
    auh_rev_obj.merchantRefNum("zyp2pt3yi8p8ag9c")
    
    response_object = optimalApiCli.card_payments_service_handler().lookup_authorization_reversal_with_merchant_no(auh_rev_obj)
    print("Authorization reversal available for provided merchant ref num. with following response: ")
    pprint(response_object,"")

def testCreateSettlement():
    #get the profile
    profile_Obj = Profile(None)
    profile_Obj.id("93d2f486-a61b-43d3-b718-d974354f244d")
    
    prof_resp_object = optimalApiCli.customer_vault_service_handler().lookup_profile(profile_Obj)
    print("Profile available with id: ", prof_resp_object.id)
    preetyPrint(prof_resp_object,"")
    
    #get the card
    card_obj = Card(None)
    card_obj.id("7262db7c-7750-4a25-963f-a5fe11999713")
    card_obj.profile(prof_resp_object)
    card_resp_obj = optimalApiCli.customer_vault_service_handler().lookup_card(card_obj)
    print("Card availabe with following response: ")
    preetyPrint(card_resp_obj,"")
    
    #get the address for shipping address detail
    address_Obj2 = Address(None)
    address_Obj2.id("acfd8c44-d76b-45ad-92a0-e8298aba7636")
    address_Obj2.profile(prof_resp_object)
    ship_add_resp_obj = optimalApiCli.customer_vault_service_handler().lookup_address(address_Obj2)
    print("Shipping address availabe with following response: ")
    preetyPrint(ship_add_resp_obj,"")
    
    
    shippingDetails_obj = ShippingDetails(None)
    shippingDetails_obj.carrier("UPS")
    shippingDetails_obj.shipMethod("N")
    shippingDetails_obj.street(ship_add_resp_obj.street)
    shippingDetails_obj.city(ship_add_resp_obj.city)
    shippingDetails_obj.state(ship_add_resp_obj.state)
    shippingDetails_obj.country(ship_add_resp_obj.country)
    shippingDetails_obj.zip("411028")
    
    
    auth_Obj = Authorization(None)
    #auth_Obj.merchantRefNum("5oc1n2jx54oqpgm0")
    auth_Obj.merchantRefNum(merchantRefNo)
    auth_Obj.amount(amount)
    auth_Obj.settleWithAuth(False)
    card_obj = Card(None)
    card_obj.paymentToken(card_resp_obj.paymentToken)
    auth_Obj.card(card_obj)
    auth_Obj.shippingDetails(shippingDetails_obj)
    
    auth_Obj.customerIp("14.140.42.67")
    auth_Obj.description("Test Authoization on card by paymenttoken")
    response_object = optimalApiCli.card_payments_service_handler().create_authorization(auth_Obj)
    print("Authorization with payment token completed with following response: ")
    preetyPrint(response_object,"")
    
    settlement_obj = Settlement(None)
    settlement_obj.merchantRefNum(merchantRefNo)
    settlement_obj.amount(amount)
    settlement_obj.authorization(response_object)
    settlement_resp_obj = optimalApiCli.card_payments_service_handler().settle_authorization(settlement_obj)
    print("Authorization with payment token completed with following response: ")
    preetyPrint(settlement_resp_obj,"")

def testLookUpSettlementById():
    settlement_obj = Settlement(None)
    settlement_obj.id("9220841f-b357-44b3-961e-e1b8abfbc2ed")
    #settlement_obj.id("72adb2a6-f072-460c-a57e-c0d1af8e4932")
    settlement_resp_obj = optimalApiCli.card_payments_service_handler().lookup_settlement_with_id(settlement_obj)
    print("Cancel settlement available with following response: ")
    preetyPrint(settlement_resp_obj,"")
    
def testCancelSettlement():
    settlement_obj = Settlement(None)
    settlement_obj.id("72adb2a6-f072-460c-a57e-c0d1af8e4932")
    settlement_obj.status("CANCELLED")
    settlement_resp_obj = optimalApiCli.card_payments_service_handler().cancel_settlement(settlement_obj)
    print("Cancel settlement completed with following response: ")
    preetyPrint(settlement_resp_obj,"")

def testLookupSettlementByMerchantRefNo():
    settlement_obj = Settlement(None)
    settlement_obj.merchantRefNum("auhkvz79bu1cptny")
    
    response_object = optimalApiCli.card_payments_service_handler().lookup_settlement_with_merchant_no(settlement_obj)
    print("Settlements available for provided merchant ref num. with following response: ")
    pprint(response_object,"")

def testCreateRefund():
    settlement_obj = Settlement(None)
    settlement_obj.id("9220841f-b357-44b3-961e-e1b8abfbc2ed")
    settlement_resp_obj = optimalApiCli.card_payments_service_handler().lookup_settlement_with_id(settlement_obj)
    print("Settlement available with following response: ")
    preetyPrint(settlement_resp_obj,"")
    
    refund_obj = Refund(None)
    refund_obj.settlements(settlement_resp_obj)
    refund_obj.merchantRefNum("cs51wkkzmwzci595")
    refund_resp_obj = optimalApiCli.card_payments_service_handler().create_refund(refund_obj)
    print("Refund completed with following response: ")
    preetyPrint(refund_resp_obj,"")
    
def testLookUpRefund():
    refund_obj = Refund(None)
    refund_obj.id("426ab43e-7511-4ff4-bdc8-bc0ab44974f1")
    refund_resp_obj = optimalApiCli.card_payments_service_handler().lookup_refund_with_id(refund_obj)
    print("Refund available with following response: ")
    preetyPrint(refund_resp_obj,"")

def testCancelRefund():
    refund_obj = Refund(None)
    refund_obj.id("426ab43e-7511-4ff4-bdc8-bc0ab44974f1")
    refund_obj.status("CANCELLED")
    refund_resp_obj = optimalApiCli.card_payments_service_handler().cancel_refund(refund_obj)
    print("Refund cancelled with following response: ")
    preetyPrint(refund_resp_obj,"")

def testLookupRefundByMerchantRefNo():
    refund_obj = Refund(None)
    refund_obj.merchantRefNum("cs51wkkzmwzci595")
    
    response_object = optimalApiCli.card_payments_service_handler().lookup_refund_with_merchant_no(refund_obj)
    print("Settlements available for provided merchant ref num. with following response: ")
    pprint(response_object,"")
    
#testPurchaseRequest()
#testLookUpAuthById()
#testReverseAuthorization()
#testAuthorizationByPaymentToken()
#testLookupAuthByMerchantRefNo()
#testCreateHeldAuthUsingCard()
#testCancelHeldAuthorization()
#testLookupAuthReversalById()
#testLookupAuthRevByMerchantRefNo()
#testCreateSettlement()
#testLookUpSettlementById()
#testCancelSettlement()
#testLookupSettlementByMerchantRefNo()
#testCreateRefund()
#testLookUpRefund()
#testLookupRefundByMerchantRefNo()
#testCancelRefund()
#testLookupAuthReversalById()
testLookupAuthRevByMerchantRefNo()
