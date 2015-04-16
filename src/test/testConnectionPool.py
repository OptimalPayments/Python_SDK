'''
Created on: 16-02-2015
@author: Anup Warke
'''

from concurrent.futures import ThreadPoolExecutor

from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from PythonNetBanxSDK.CustomerVault.Profile import Profile
from PythonNetBanxSDK.CustomerVault.Addresses import Address
from PythonNetBanxSDK.HostedPayment.Order import Order


api_key = 'devcentre4628'
api_password = 'B-qa2-0-548ef25d-302b0213119f70d83213f828bc442dfd0af3280a7b48b1021400972746f9abe438554699c8fa3617063ca4c69a'
account_number = '89983472'


optimalApiCli = OptimalApiClient(api_key,api_password, "TEST", account_number)

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

def callHostedServices(req_data,requestNo):
    print("Request : ", requestNo, " =>")
    response_object = optimalApiCli.hosted_payment_service_handler().get_order(req_data)
    print("response received for request no:", requestNo)
    #print("Order available with id :", response_object.id)
    #preetyPrint(response_object,"")

def callExecutor(order_obj):
    print("Called")
    executor.submit(callHostedServices,order_obj,0); 
        
future_result = [];
executor = ThreadPoolExecutor(max_workers=15)
#for i in range(0,30):
#    #Lookup Order
#    order_obj = Order(None)
#    order_obj.id("27CIQ2PYS77JK851L0")
#    future = executor.submit(callHostedServices,order_obj,i);
#    future_result.append(future)
#    ecep = future.exception(2000);
#    print("Error with request-", i," =>", ecep)
order_obj_arr = []

for i in range(0,20):
    order_obj = Order(None)
    order_obj.id("27CIQ2PYS77JK851L0")
    order_obj_arr.append(order_obj)
    
list(map(callExecutor, order_obj_arr))
