from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient

from PythonNetBanxSDK.common.DomainObject import DomainObject
from test.RandomTokenGenerator import RandomTokenGenerator
from PythonNetBanxSDK.HostedPayment.Order import Order
from PythonNetBanxSDK.HostedPayment.Transaction import Transaction
from PythonNetBanxSDK.HostedPayment.Settlement import Settlement
from PythonNetBanxSDK.CustomerVault.Profile import Profile
from PythonNetBanxSDK.CustomerVault.Addresses import Address
from PythonNetBanxSDK.CardPayments.CardExpiry import CardExpiry
from PythonNetBanxSDK.CustomerVault.Card import Card
from PythonNetBanxSDK.HostedPayment.ExtendedOptions import ExtendedOptions


api_key = 'devcentre4628'
api_password = 'B-qa2-0-548ef25d-302b0213119f70d83213f828bc442dfd0af3280a7b48b1021400972746f9abe438554699c8fa3617063ca4c69a'
account_number = '89983472'

optimalApiCli = OptimalApiClient(api_key,api_password, "TEST", account_number)
tokenGenerator = RandomTokenGenerator()
#mykey = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(16))

merchantRefNum = tokenGenerator.generateToken()
totalAmount = 1044

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

def testCreateOrder():
    order_obj = Order(None)
    order_obj.customerIp("14.140.42.67")
    order_obj.merchantRefNum(merchantRefNum)
    order_obj.currencyCode("USD")
    order_obj.totalAmount(totalAmount)
    order_obj.customerNotificationEmail("test2@abcd.com")
    order_obj.merchantNotificationEmail("test4@abcd.com")
    
    response_object = optimalApiCli.hosted_payment_service_handler().create_order(order_obj)
    print("Order created with id: ", response_object.id)
    preetyPrint(response_object,"")
   
def testCreateOrderWithProfile():
    # Get the profile
    profile_Obj = Profile(None)
    profile_Obj.id("93d2f486-a61b-43d3-b718-d974354f244d")
    
    prof_respo = optimalApiCli.customer_vault_service_handler().lookup_profile(profile_Obj)
    print("Profile available with id:" ,prof_respo.id)
    preetyPrint(prof_respo,"")
    
    
    order_obj = Order(None)
    order_obj.customerIp("14.140.42.67")
    order_obj.merchantRefNum(merchantRefNum)
    order_obj.currencyCode("USD")
    order_obj.totalAmount(totalAmount)
    order_obj.profile(profile_Obj)
    order_obj.customerNotificationEmail("test2@abcd.com")
    
    response_object = optimalApiCli.hosted_payment_service_handler().create_order(order_obj)
    print("Order created with id: ", response_object.id)
    preetyPrint(response_object,"")   


def testGetOrder():
    
    order_obj = Order(None)
    #order_obj.id("27CIQ2PYS77JK851L0")
    
    #print("Create order Data for request : ", requestNo, " =>")
    #response_object = optimalApiCli.hosted_payment_service_handler().create_order(order_obj)
    #print("Order created with id: ", response_object.id)
    
    #get_order_obj = Order(None)
    #get_order_obj.id(response_object.id)
    response_object = optimalApiCli.hosted_payment_service_handler().get_order(order_obj)
    preetyPrint(response_object,"")
    if (response_object.extendedOptions):
        print(response_object.extendedOptions[0].__dict__)
    
def testUpdateOrder():
    order_obj = Order(None)
    order_obj.id("27CIQ2PYS77JK851L0")
    txnObj = Transaction(None)
    txnObj.status("success")
    order_obj.transaction(txnObj)
    
    #print("Create order Data for request : ", requestNo, " =>")
    #response_object = optimalApiCli.hosted_payment_service_handler().create_order(req_data)
    #print("Order created with id: ", response_object.id)
    
    #get_order_obj = Order(None)
    #get_order_obj.id(response_object.id)
    #response_object = optimalApiCli.hosted_payment_service_handler().get_order(get_order_obj)
    
    #update_order_obj = Order(None)
    #update_order_obj.id(response_object.id)
    response_object = optimalApiCli.hosted_payment_service_handler().update_order(order_obj)
    print("Order updated with id :", response_object.id)
    preetyPrint(response_object,"")
    
def testCancelOrder():
    order_obj = Order(None)
    order_obj.id("27CIQ2PYS77JK851L0")
    response_object = optimalApiCli.hosted_payment_service_handler().cancel_order(order_obj)
    print("Order canceled with id :", response_object.id)
    preetyPrint(response_object,"")
    
def testCancelOrderWithoutTransaction():
    # Get the profile
    profile_Obj = Profile(None)
    profile_Obj.id("93d2f486-a61b-43d3-b718-d974354f244d")
    
    prof_respo = optimalApiCli.customer_vault_service_handler().lookup_profile(profile_Obj)
    print("Profile available with id:" ,prof_respo.id)
    preetyPrint(prof_respo,"")
    
    
    order_obj = Order(None)
    order_obj.customerIp("14.140.42.67")
    order_obj.merchantRefNum(merchantRefNum)
    order_obj.currencyCode("USD")
    order_obj.totalAmount(totalAmount)
    order_obj.profile(profile_Obj)
    order_obj.customerNotificationEmail("test2@abcd.com")
    
    response_object = optimalApiCli.hosted_payment_service_handler().create_order(order_obj)
    print("Order created with id: ", response_object.id)
    preetyPrint(response_object,"")      
    
    
    order_obj2 = Order(None)
    order_obj2.id(response_object.id)
    response_object = optimalApiCli.hosted_payment_service_handler().cancel_order(order_obj2)
    print("Order canceled with id :", response_object.id)
    preetyPrint(response_object,"")
    
    
def testCreateOrderWithPaymenttoken():    
    # Get the profile
    profile_Obj = Profile(None)
    profile_Obj.id("ed853368-b876-4928-8312-69eb7739f3b9")
    profile_Obj.paymentToken("Px6Fuqsw52UiFNt")
   
    # Address with Argentina
    #addr_obj = Address(None)
    #addr_obj.country("AR")
    #addr_obj.city("Buenos Aires")
    #addr_obj.street("Carlos Pellegrini 551")
    #addr_obj.street2("1009 Buenos Aires")
    #addr_obj.zip("C1009ABK")
    #profile_obj = Profile(prof_respo)
    #addr_obj.profile(profile_obj)
    
    #addr_respo = optimalApiCli.customer_vault_service_handler().create_address(addr_obj)

    #addr_respo = optimalApiCli.customer_vault_service_handler().lookup_address(addr_respo)
    #print("Address available with id:" , addr_respo.id)
    #preetyPrint(prof_respo,"")
    
    # Card with Argentina
    #card_obj = Card(None)
    #card_obj.nickName("John's corporate Visa")
    #card_obj.holderName("MR. JOHN SMITH")
    #card_obj.cardNum("4530910000012345")
    #card_obj.billingAddressId(addr_respo.id)
    #card_obj.defaultCardIndicator("true")
    #card_exp_obj = CardExpiry(None)
    #card_exp_obj.month("12")
    #card_exp_obj.year("2019")
    
    #profile_obj = Profile(prof_respo)
    #card_obj.profile(profile_obj)
    #card_obj.cardExpiry(card_exp_obj)

    #card_respo = optimalApiCli.customer_vault_service_handler().create_card(card_obj)
    
    #card_respo = optimalApiCli.customer_vault_service_handler().lookup_address(card_respo)
    #print("Address available with id:" , card_respo.id)
    #preetyPrint(prof_respo,"")
        
    # Order with exptended options
    order_obj = Order(None)
    order_obj.customerIp("14.140.42.67")
    order_obj.merchantRefNum(merchantRefNum)
    order_obj.currencyCode("USD")
    order_obj.totalAmount(totalAmount)
    
    #profile_obj1 = Profile(None)
    #profile_obj1.id(prof_respo.id)
    order_obj.profile(profile_Obj)
    
    #order_obj.paymentToken(card_obj.paymentToken)
    order_obj.customerNotificationEmail("test2@abcd.com")
    
    eolist = []
    eo = ExtendedOptions(None)
    eo.key("authType")
    eo.value("auth")
    eolist.append(eo)
    order_obj.extendedOptions(eolist)
    
    response_object = optimalApiCli.hosted_payment_service_handler().create_order(order_obj)
    print("Order created with id: ", response_object.id)
    preetyPrint(response_object,"")      
    
def testSettlementOfOrder():
    order_obj = Order(None)
    order_obj.id("27CIQ2PYS77JK851L0")
    
    order_resp_obj = optimalApiCli.hosted_payment_service_handler().get_order(order_obj)
    print("Order available with id :", order_resp_obj.id)
    preetyPrint(order_resp_obj,"")
    
    settlement_obj = Settlement(None)
    settlement_obj.order(order_resp_obj)
    settlement_obj.amount(totalAmount)
    settlement_obj.merchantRefNum(merchantRefNum)
    
    settlement_resp_obj = optimalApiCli.hosted_payment_service_handler().settle_order(settlement_obj)
    print("Settlement completed with following resposne")
    preetyPrint(settlement_resp_obj,"")
    

    
    
#testCreateOrder()
testGetOrder()
#testUpdateOrder()
#testGetOrder()
#testCreateOrderWithProfile()
#testCancelOrder()
#testCancelOrderWithoutTransaction()
#testCreateOrderWithPaymenttoken()
#testSettlementOfOrder()
