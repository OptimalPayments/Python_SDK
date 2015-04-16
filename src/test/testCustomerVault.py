from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from PythonNetBanxSDK.CustomerVault.Profile import Profile
from PythonNetBanxSDK.CustomerVault.Addresses import Address
from PythonNetBanxSDK.CardPayments.Card import Card
from PythonNetBanxSDK.CardPayments.CardExpiry import CardExpiry

from PythonNetBanxSDK.HostedPayment.Order import Order

from copy import deepcopy
from PythonNetBanxSDK.Environment import Environment

from PythonNetBanxSDK.HostedPayment.Order import Order

from concurrent.futures import ThreadPoolExecutor

api_key = 'devcentre4628'
api_password = 'B-qa2-0-548ef25d-302b0213119f70d83213f828bc442dfd0af3280a7b48b1021400972746f9abe438554699c8fa3617063ca4c69a'
account_number = '89983472'

optimalApiCli = OptimalApiClient(api_key,api_password, "TEST", account_number)

def preetyPrint(resObj, tabSpace):
    print("type====>",type(resObj))
    if (isinstance(resObj,str)):
        print(tabSpace,"[",resObj,"]")
    elif resObj.__dict__ is not None:
        print(tabSpace,"Printing Details for :", type(resObj))
        for key in resObj.__dict__:
            if (isinstance(resObj.__dict__[key],dict)):
                preetyPrint(resObj.__dict__[key],"  ")
            elif (isinstance(resObj.__dict__[key],list)):
                for c in range(0, resObj.__dict__[key].__len__()):
                    preetyPrint(resObj.__dict__[key][c],"  ")
            else:
                print(tabSpace, "     ", key, " = ", resObj.__dict__[key])
                
def createProfile():
    profile_Obj = Profile(None)
    profile_Obj.merchantCustomerId("mycustomer0192036")
    profile_Obj.locale("en_US")
    profile_Obj.firstName("sachin")
    profile_Obj.lastName("tendulkar")
    profile_Obj.email("sachin.tendulkar@somedomain.com")
    profile_Obj.phone("713-587-5556")
    response_object = optimalApiCli.customer_vault_service_handler().create_profile(profile_Obj)
    print("Profile created with id: ", response_object.id)
    preetyPrint(response_object,"")

def testGetProfile():
    profile_Obj = Profile(None)
    profile_Obj.id("93d2f486-a61b-43d3-b718-d974354f244d")
    
    response_object = optimalApiCli.customer_vault_service_handler().lookup_profile(profile_Obj)
    print("Profile available with id: ", response_object.id)
    preetyPrint(response_object,"")

def createAddress():
    profile_Obj = Profile(None)
    profile_Obj.id("ed853368-b876-4928-8312-69eb7739f3b9")
    
    prof_respo = optimalApiCli.customer_vault_service_handler().lookup_profile(profile_Obj)
    print("Profile available with id:" ,prof_respo.id)
    preetyPrint(prof_respo,"")
    
    if prof_respo.id is not None:
        address_Obj = Address(None)
        address_Obj.nickName("heldadd")
        address_Obj.street("100 Queen Street West")
        address_Obj.street2("Unit 201")
        address_Obj.city("Toronto")
        address_Obj.country("AR")
        address_Obj.state("ON")
        address_Obj.zip("C1009ABK")
        address_Obj.recipientName("suresh")
        address_Obj.phone("647-788-3901")
        address_Obj.profile(prof_respo)
        print("Profile id:  " , address_Obj.profile.id)
        response_object = optimalApiCli.customer_vault_service_handler().create_address(address_Obj)
        print("Address created with id: ", response_object.id)
        preetyPrint(response_object,"")
    else:    
        print("Without profile an address cann't be created")

def testLookupAddress():
    profile_Obj = Profile(None)
    profile_Obj.id("93d2f486-a61b-43d3-b718-d974354f244d")
    
    prof_respo = optimalApiCli.customer_vault_service_handler().lookup_profile(profile_Obj)
    print("Profile available with id:" ,prof_respo.id)
    
    address_Obj = Address(None)
    address_Obj.id("8411776b-bc59-4a3b-97dc-b6a6b879bb76")
    address_Obj.profile(prof_respo)
    add_resp_obj = optimalApiCli.customer_vault_service_handler().lookup_address(address_Obj)
    print("Address availabe with following response: ")
    preetyPrint(add_resp_obj,"")


def testCreateCards():
    profile_Obj = Profile(None)
    profile_Obj.id("ed853368-b876-4928-8312-69eb7739f3b9")
    
    prof_respo = optimalApiCli.customer_vault_service_handler().lookup_profile(profile_Obj)
    print("Profile available with id:" ,prof_respo.id)
    if prof_respo.id is not None:
        card_obj = Card(None)
        card_obj.cardNum("3569990000000009")
        cardExpiry_obj = CardExpiry(None)
        cardExpiry_obj.month("06")
        cardExpiry_obj.year("2018")
        card_obj.cardExpiry(cardExpiry_obj)
        card_obj.profile(prof_respo)
        response_object = optimalApiCli.customer_vault_service_handler().create_card(card_obj)
        print("Created created with id: ", response_object.id, "& Status", response_object.status)
        preetyPrint(response_object,"")
        
        print("response_object.cardExpiry.month: " , response_object.cardExpiry.month)
        print("response_object.cardExpiry.year: " , response_object.cardExpiry.year)
    else:    
        print("Without profile a card cann't be created")

def testGetProfileSubCompo():
    profile_Obj = Profile(None)
    profile_Obj.id("93d2f486-a61b-43d3-b718-d974354f244d")
    
    response_object = optimalApiCli.customer_vault_service_handler().lookup_profile_subcomponents(profile_Obj, True, True)
    print("Profile available with id: ", response_object.id)
    preetyPrint(response_object,"")

def testUpdateCard():
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
    
    #update the card for billing address
    card_obj2 = Card(None)
    card_obj2.id("7262db7c-7750-4a25-963f-a5fe11999713")
    card_obj2.profile(prof_resp_object)
    card_obj2.billingAddressId("f67a220a-bfec-4a5b-a7f0-4c15abfc62c8") 
    cardExpiry_obj = CardExpiry(None)
    cardExpiry_obj.month(card_resp_obj.cardExpiry.month)
    cardExpiry_obj.year(card_resp_obj.cardExpiry.year)
    card_obj2.cardExpiry(cardExpiry_obj)
    card_resp_obj2 = optimalApiCli.customer_vault_service_handler().update_card(card_obj2)
    print("Card updated with following response: ")
    preetyPrint(card_resp_obj2,"")
    
def testCreateCardForRiskTrns():
    profile_Obj = Profile(None)
    profile_Obj.id("93d2f486-a61b-43d3-b718-d974354f244d")
    
    prof_respo = optimalApiCli.customer_vault_service_handler().lookup_profile(profile_Obj)
    print("Profile available with id:" ,prof_respo.id)
    if prof_respo.id is not None:
        #create an address with risk teretories
        #address_Obj = Address(None)
        #address_Obj.nickName("heldAdd")
        #address_Obj.street("102 king Street east")
        #address_Obj.street2("Unit 401")
        #address_Obj.city("Buenos Aires")
        #address_Obj.country("AR")
        #address_Obj.state("BA")
        #address_Obj.zip("C1009ABK")
        #address_Obj.recipientName("heldAddpay")
        #address_Obj.phone("647-799-3901")
        #address_Obj.profile(prof_respo)
        #print("Profile id:  " , address_Obj.profile.id)
        #hel_add_resp_obj = optimalApiCli.customer_vault_service_handler().create_address(address_Obj)
        #print("held Address created with id: ", hel_add_resp_obj.id)
        #preetyPrint(hel_add_resp_obj,"")
        
        #if(hel_add_resp_obj.error):
        #    print("===========Error while address creation ================")
        #else:
        card_obj = Card(None)
        card_obj.cardNum("4510150000000321")
        cardExpiry_obj = CardExpiry(None)
        cardExpiry_obj.month("08")
        cardExpiry_obj.year("2020")
        card_obj.cardExpiry(cardExpiry_obj)
        card_obj.profile(prof_respo)
        card_obj.billingAddressId("8411776b-bc59-4a3b-97dc-b6a6b879bb76") 
        #card_obj.billingAddressId(hel_add_resp_obj.id) 
        held_card_cr_resp_obj = optimalApiCli.customer_vault_service_handler().create_card(card_obj)
        print("Created created with id: ", held_card_cr_resp_obj.id, "& Status", held_card_cr_resp_obj.status)
        preetyPrint(held_card_cr_resp_obj,"")
    else:    
        print("Without profile a card cann't be created")
    
#createProfile()
#testGetProfile()
#testGetProfileSubCompo()
#createAddress()
#testLookupAddress()
testCreateCards()

#testUpdateCard()
#testCreateCardForRiskTrns()