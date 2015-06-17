'''
Created on 10-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.OptimalApiClient import OptimalApiClient
from PythonNetBanxSDK.HostedPayment.Order import Order
from PythonNetBanxSDK.HostedPayment.Transaction import Transaction
from PythonNetBanxSDK.CustomerVault.Profile import Profile
from PythonNetBanxSDK.HostedPayment.Settlement import Settlement
from PythonNetBanxSDK.HostedPayment.ExtendedOptions import ExtendedOptions
from PythonNetBanxSDK.HostedPayment.Redirect import Redirect
from RandomTokenGenerator import RandomTokenGenerator
from pprint import pprint
from PythonNetBanxSDK.HostedPayment.Refund import Refund


class SampleTest_Hosted(object):
    '''
    classdocs
    '''

    _api_key = 'devcentre4628'
    _api_password = 'B-qa2-0-548ef25d-302b0213119f70d83213f828bc442dfd0af3280a7b48b1021400972746f9abe438554699c8fa3617063ca4c69a'
    _account_number = '89983472'

    def __init__(self):
        '''
        Constructor
        '''
        # OptimalApiClient Object
        self.optimalApiCli = OptimalApiClient(self._api_key, 
                                         self._api_password, 
                                         "TEST", 
                                         self._account_number)


    def hosted_payment_monitor(self):
        '''
        Hosted Payment Monitor
        '''
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).monitor()
        print ("response object : ")
        print (response_object.status)   
  
    def create_order(self):
        '''
        Create Order
        27CIQ2AQY2G5JY31LQ
        8d1457c5-d3be-4ebe-919c-accded13a568
        '''
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

       
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).create_order(order_obj)    
                                                 
        print ("Create Order Response: ")
        print (response_object.__dict__)

    def create_profile_with_order(self):
        '''
        Create Profile with Order
        '''
        order_obj = Order(None)
        order_obj.merchantRefNum(str(RandomTokenGenerator().generateToken()))
        order_obj.currencyCode("USD")
        order_obj.totalAmount(1000)

        profile_obj = Profile(None)
        profile_obj.merchantCustomerId(str(RandomTokenGenerator().generateToken()))
        profile_obj.firstName("Jane")
        profile_obj.lastName("Smythe")
        order_obj.profile(profile_obj)
		
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).create_order(order_obj)    
                                                 
        print ("Create Order Response: ")
        print (response_object.__dict__)
		

    def silent_post(self):
        '''
        Create Order
        27CIQ2AQY2G5JY31LQ
        8d1457c5-d3be-4ebe-919c-accded13a568
        '''
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
        
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).create_order(order_obj)    
                                                 
        print ("Create Order Response: ")
        print (response_object.__dict__)

     
 
    def process_order_with_payment_token(self):
        '''
        Process order with payment token
        '''
        order_obj = Order(None)
        order_obj.customerIp("14.140.42.67")
        order_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        order_obj.currencyCode("USD")
        order_obj.totalAmount("2006")
        order_obj.customerNotificationEmail("jane.smythe@emailhost.com")
        
        profile_obj = Profile(None)
        profile_obj.id("ee2c3dc6-022c-4d7e-a1ab-685cf28c7aad")
        profile_obj.paymentToken("Pff1PwG5LFuiq5q")
        order_obj.profile(profile_obj)
        
#        eo_list = []
#        eo = ExtendedOptions(None)
#        eo.key("silentPost")
#        eo.value("true")
#        eo_list.append(eo)
#        order_obj.extendedOptions(eo_list)
        
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, 
                                             env="TEST", 
                                             account_number=self._account_number)
        print("===", self._optimal_obj.to_dictionary(order_obj))
        
        
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).create_order(order_obj)    
                                                 
        print ("Create Order Response: ")
        print (response_object)
    

    def process_order_with_profile_id(self):
        '''
        Process an order with profile Id
        '''
        order_obj = Order(None)
        order_obj.customerIp("14.140.42.67")
        order_obj.merchantRefNum(str(RandomTokenGenerator().generateToken()))
        order_obj.currencyCode("USD")
        order_obj.totalAmount("3000")
        order_obj.customerNotificationEmail("abc.pqr@emailhost.com")
        profile_obj = Profile(None)
        profile_obj.id("fe141eb8-00a3-4725-83f2-b1e5cbe8b817")
        order_obj.profile(profile_obj)


        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).create_order(order_obj)    
                                                 
        print ("Create Order Response: ")
        print (response_object)     
        print (response_object.profile.firstName)


    def process_order_with_hosted_page(self):
        order_obj = Order(None)
        order_obj.customerIp("14.140.42.67")
        order_obj.merchantRefNum(str(RandomTokenGenerator().generateToken()))
        order_obj.currencyCode("USD")
        order_obj.totalAmount("2000")
        order_obj.customerNotificationEmail("jane.smythe@emailhost.com")        

        response_object = self.optimalApiCli.hosted_payment_service_handler().create_order(order_obj)
        
        print ("Process order with hosted page: ")
        print(response_object.__dict__)


    def get_order(self):
        '''
        Get Order
        27CIQ2ANJ7AORAF1LS
        fd1fbb53-2a7d-49fc-9ca0-b4f48ad74e23
        '''
        order_obj = Order(None)
        order_obj.id("27CIQ2P65LDFRZF1LZ")
        print ("request data:", order_obj.__dict__)
         
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).get_order(order_obj)    
                   
        print ("Create Order Response: ")
        print (response_object.__dict__)    

        for c in range(0, response_object.link.__len__()):
            print ('link-rel: ', response_object.link[c].rel)
            print ('link-uri: ', response_object.link[c].uri)


    def get_order_report(self):
        '''
        Get Order Report
        '''
        order_obj = Order(None)
		
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).get_order_report(order_obj, "5", "0")	
		
        print ("Response Object : ", response_object)
        print ("Length : ", response_object.__len__())
        for c in range(0, response_object.__len__()):
            print ('Records : ', c)
            print ('Order Id : ', response_object[c].id)
            print ('Merchant Reference Number :', response_object[c].merchantRefNum)
            print ('Currency Code : ', response_object[c].currencyCode)
            print ('Total Amount : ', response_object[c].totalAmount)

			
    def update_order(self):
        '''
        Update Order
        27CIQ2ANJ7AORAF1LS
        fd1fbb53-2a7d-49fc-9ca0-b4f48ad74e23
        '''
        
        order_obj = Order(None)
        order_obj.id("27CIQ2PTEWISYYP1L8")
        #order_obj.currencyCode("CAD")
        
        #order_obj.id("27CIQ2KBVDHTB3N1L7")
        trans_obj = Transaction(None)
        trans_obj.status("successe")
        #trans_obj.status("cancelled")
        order_obj.transaction(trans_obj)
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).update_order(order_obj)    
        
        print ("Create Order Response: ")
        print (response_object)


    def update_rebill_order(self):
        '''
        Update Order
        27CIQ2ANJ7AORAF1LS
        fd1fbb53-2a7d-49fc-9ca0-b4f48ad74e23
        '''
        
        order_obj = Order(None)
        order_obj.id("27CIQ2PTE52FWSJ1LK")
        #order_obj.currencyCode("CAD")
        
        #order_obj.id("27CIQ2KBVDHTB3N1L7")
        trans_obj = Transaction(None)
        trans_obj.status("success")
        #trans_obj.status("cancelled")
        order_obj.transaction(trans_obj)
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).update_order(order_obj)    
        
        print ("Create Order Response: ")
        print (response_object)


    def cancel_order(self):
        '''
        27CIQ2J6RJ7LXTL1LJ
        Cancel Order
        27CIQ2ANJ7AORAF1LS
        fd1fbb53-2a7d-49fc-9ca0-b4f48ad74e23
        '''
        order_obj = Order(None)
        order_obj.id("27CIQ2PTEWISYYP1L9")
        print ("request data:", order_obj.__dict__)
         
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).cancel_order(order_obj)    
         
        print ("Create Order Response: ")
        print (response_object)
 
 
    def settle_order(self):
        '''
        27CIQ2P4R4DD89Z1LB
        Settle an Order
        '''
        settle_obj = Settlement(None)
        settle_obj.amount("2004")
        settle_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        order_obj = Order(None)
        order_obj.id("27CIQ2PTEWISYYP1L8")
        settle_obj.order(order_obj)
        
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).settle_order(settle_obj)    
         
        print ("Create Order Response: ")
        print (response_object)
 
 
 
    def refund_order(self):
        '''
        Settle an Order
        '''
        refund_obj = Refund(None)
        refund_obj.amount("2004")
        refund_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        order_obj = Order(None)
        order_obj.id("127CIQ2P4R4DD89Z1LB")
        refund_obj.order(order_obj)
        
        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, 
                                             env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).refund_order(refund_obj)    
         
        print ("Response: ")
        print (response_object)
  

    def process_rebill_using_id(self):
        order_obj = Order(None)
        order_obj.id("27CIQ2PTEWISYYP1L8")
        order_obj.totalAmount("2004")
        order_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        order_obj.currencyCode("USD")

        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, 
                                             env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).process_rebill_using_order_id(order_obj)    
         
        print ("Response: ")
        print (response_object.__dict__)
        

    def process_rebill_using_due_date(self):
        order_obj = Order(None)
        order_obj.id("27CIQ2PTEWISYYP1L8")
        order_obj.dueDate("2014-09-24")
        order_obj.totalAmount("2004")
        order_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        order_obj.currencyCode("USD")

        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, 
                                             env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).process_rebill_using_order_id(order_obj)    
         
        print ("Response: ")
        print (response_object)

    def process_rebill_using_Profile(self):
        order_obj = Order(None)
        profile_obj = Profile(None)
        #order_obj.id("27CIQ2PTEWISYYP1L8")
        order_obj.dueDate("2018-09-24")
        order_obj.totalAmount("200")
        profile_obj.id("91b65e7f-c800-4f52-861a-6bd921ba3831")
        profile_obj.paymentToken("CT7uSUOJ550zMBW")
        order_obj.profile(profile_obj)
        order_obj.merchantRefNum(RandomTokenGenerator().generateToken())
        order_obj.currencyCode("USD")
        eo_list = []
        eo = ExtendedOptions(None)
        eo.key("recurringIndicator")
        eo.value(True)
        eo_list.append(eo)
        order_obj.extendedOptions(eo_list)

        self._optimal_obj = OptimalApiClient(api_key=self._api_key,
                                             api_password=self._api_password, 
                                             env="TEST", 
                                             account_number=self._account_number)
        response_object = self._optimal_obj.hosted_payment_service_handler(
                                            ).process_rebill_using_profile_id(order_obj)    
         
        print ("Response: ")
        print (response_object)

#o = SampleTest_Hosted().create_order()
#o = SampleTest_Hosted().process_rebill_using_Profile() 
#o = SampleTest_Hosted().process_order_with_payment_token()
#o = SampleTest_Hosted().get_order()
o = SampleTest_Hosted().create_profile_with_order()
#o = SampleTest_Hosted().update_order()
#o = SampleTest_Hosted().settle_order()
#o = SampleTest_Hosted().refund_order()
#o = SampleTest_Hosted().process_rebill_using_id()
#o = SampleTest_Hosted().process_rebill_using_due_date()