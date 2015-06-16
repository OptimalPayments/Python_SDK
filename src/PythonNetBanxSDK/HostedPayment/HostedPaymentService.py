'''
Created on 30-Jan-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK import HostedPayment
from PythonNetBanxSDK import common


class HostedPaymentService(object):
    '''
    classdocs
    '''
    # Define URL paths for Order
    _MONITOR_PATH = '/hosted/monitor'
    _URI = '/hosted/v1'
    _ORDER_PATH = '/orders'
    _RESEND_CALLBACK = '/resend_callback/'
    _REFUND_PATH = '/refund'
    _SETTLEMENT_PATH = '/settlement'
    _URI_SEPARATOR = '/'

    # SUB-COMPONENTS
    _NUM = '?num='
    _START = '&start='
                 
    def __init__(self, optimal_object):
        '''
        Constructor
        '''
        # OptimalApiClient Object
        self.optimal_object = optimal_object
        
    '''
    Prepare URL for process request
    @param: Chunks of paths
    @return: Complete URL for Processing Request
    '''
    def _prepare_uri(self, path):
        return self._URI + path
    
    '''
    Prepare Error Response
    @param: response object, class name
    @return: object of class
    '''    
    def prepare_error(self, class_name, error_code, error_message):
        error_object_response = class_name(None)
        error_obj = common.Error.Error(None)
        error_obj.code(error_code)
        error_obj.message(error_message)
        error_object_response.error(error_obj.__dict__)
        return (error_object_response)    
    
    '''
    Process the response from the Server
    @param: response object, class name
    @return: object of class
    '''
    def _process_response(self, response, class_name):
        if isinstance(response, int):
            response_status = class_name(None)
            response_status.status = response
            return (response_status)
        elif response is None:
            return class_name(None)
        elif isinstance(response, common.Error.Error):
            return self.prepare_error(class_name, response.code, response.message)
        else:
            return (class_name(response))


    '''
    Monitor
    
    @param: None
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    def monitor(self):
        FULL_URL = self._MONITOR_PATH
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET",
                                                url=FULL_URL,
                                                data=None)   
        return (self._process_response(response, HostedPayment.Order.Order))
    
    '''
    Create an Order
    
    @param: Order object
    @return: Order object
    @raise: IOException
    @raise: OptimalException 
    '''
    def create_order(self, data):
        FULL_URL = self._prepare_uri(self._ORDER_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST", 
                                                url=FULL_URL, 
                                                data=data)    
        return (self._process_response(response, HostedPayment.Order.Order))

    
    '''
    Get an Order
    
    @param: Order Id
    @return: Order object
    @raise: IOException
    @raise: OptimalException 
    '''
    def get_order(self, data):
        try:
            order_id = data.id
            del data.id
        except AttributeError as e:
            err_msg = "Attribute Error: " + str(e) + " not available"
            return (self.prepare_error(HostedPayment.Order.Order, 
                                       "400", 
                                       err_msg))
        FULL_URL = self._prepare_uri(self._ORDER_PATH + \
                                     self._URI_SEPARATOR + \
                                     order_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)
        return (self._process_response(response, HostedPayment.Order.Order))

    
    '''
    Update an Order
    
    @param: Order Id, Order object
    @return: Order
    @raise: IOException
    @raise: OptimalException
    '''
    def update_order(self, data):
        try:
            order_id = data.id
            del data.id
        except AttributeError as e:
            err_msg = "Attribute Error: " + str(e) + " not available"
            return (self.prepare_error(HostedPayment.Order.Order, 
                                       "400", 
                                       err_msg))
        FULL_URL = self._prepare_uri(self._ORDER_PATH + \
                                     self._URI_SEPARATOR + \
                                     order_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)
        return (self._process_response(response, HostedPayment.Order.Order))

    
    '''
    Cancel an Order
    
    @param: Order Id
    @return: Response Status Code
    @raise: IOException
    @raise: OptimalException
    '''
    def cancel_order(self, data):
        try:
            order_id = data.id
            del data.id
        except AttributeError as e:
            err_msg = "Attribute Error: " + str(e) + " not available"
            return (self.prepare_error(HostedPayment.Order.Order, 
                                       "400", 
                                       err_msg))
        FULL_URL = self._prepare_uri(self._ORDER_PATH + \
                                     self._URI_SEPARATOR + \
                                     order_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None)
        return (self._process_response(response, HostedPayment.Order.Order))

    
    '''
    Cancel held Order
    
    @param: Order Id, Order object
    @return: Order object
    @raise: IOException
    @raise: OptimalException
    '''
    def cancel_held_order(self, data):
        try:
            order_id = data.id
            del data.id
        except AttributeError as e:
            err_msg = "Attribute Error: " + str(e) + " not available"
            return (self.prepare_error(HostedPayment.Order.Order, 
                                       "400", 
                                       err_msg))
        FULL_URL = self._prepare_uri(self._ORDER_PATH + \
                                     self._URI_SEPARATOR + \
                                     order_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)
        return (self._process_response(response, HostedPayment.Order.Order))

    
    '''
    Cancel a Settlement Order
    
    @param: Order Id, Order Object
    @return: Order object
    @raise: IOException
    @raise: OptimalException
    '''
    def cancel_settlement_order(self, data):
        response = self.cancel_order(data)
        return (response)

    
    '''
    Refund an Order
    
    @param: Order Id, Refund object
    @return: Refund object
    @raise: IOException
    @raise: OptimalException
    '''
    def refund_order(self, data):
        try:
            order_id = data.order.id
            del data.order
        except AttributeError as e:
            err_msg = "Attribute Error: " + str(e) + " not available"
            return (self.prepare_error(HostedPayment.Refund.Refund, 
                                       "400", 
                                       err_msg))
        FULL_URL = self._prepare_uri(self._ORDER_PATH + \
                                     self._URI_SEPARATOR + \
                                     order_id + \
                                     self._REFUND_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST", 
                                                url=FULL_URL, 
                                                data=data)
        return (self._process_response(response, HostedPayment.Refund.Refund))
   
   
    '''
    Settle an Order
   
    @param: Order Id, Settlement object
    @return: Settlement object
    @raise: IOException
    @raise: OptimalException
    '''
    def settle_order(self, data):
        try:
            order_id = data.order.id
            del data.order
        except AttributeError as e:
            err_msg = "Attribute Error: " + str(e) + " not available"
            return (self.prepare_error(HostedPayment.Settlement.Settlement, "400", err_msg))
        FULL_URL = self._prepare_uri(self._ORDER_PATH + self._URI_SEPARATOR + \
                                     order_id + self._SETTLEMENT_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(req_method="POST", 
                                                       url=FULL_URL, 
                                                       data=data)
        return (self._process_response(response, HostedPayment.Settlement.Settlement))

    
    '''
    Get an Order Report
    
    @param: Order data, Number of Records, Starting Index
    @return: List of Order objects
    @raise: IOException
    @raise: OptimalException
    '''
    def get_order_report(self, data, numOfRecords, startIndex):
        if numOfRecords is None:
            num = '2'
        else:
            num = numOfRecords
        if startIndex is None:
            start = '2'
        else:
            start = startIndex
        FULL_URL = self._prepare_uri(self._ORDER_PATH + self._NUM + num + \
                                     self._START + start)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(req_method="GET", 
                                                       url=FULL_URL, 
                                                       data=None)
        order_list = []
        if (response["records"].__len__() == 0):
            return (order_list)
        else:
            for count in range(0,response["records"].__len__()):
                order_list.append(
                            self._process_response(response["records"][count],
                            HostedPayment.Order.Order))
            return (order_list)

    
    '''
    Resend callback
    
    @param: Order Id
    @return: Status (Success or Fail)
    @raise: IOException
    @raise: OptimalException
    '''
    def resend_callback(self, data):
        try:
            order_id = data.id
            del data.id
        except AttributeError as e:
            err_msg = "Attribute Error: " + str(e) + " not available"
            return (self.prepare_error(HostedPayment.Order.Order, 
                                       "400", 
                                       err_msg))
        FULL_URL = self._prepare_uri(self._ORDER_PATH + \
                                     self._URI_SEPARATOR + \
                                     order_id + \
                                     self._RESEND_CALLBACK)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)
        return (self._process_response(response, HostedPayment.Order.Order))

    
    '''
    Process a rebill using Order Id
    
    @param: Order Id, Order object
    @return: Order object
    @raise: IOException
    @raise: OptimalException
    '''
    def process_rebill_using_order_id(self, data):
        try:
            order_id = data.id
            del data.id
        except AttributeError as e:
            err_msg = "Attribute Error: " + str(e) + " not available"
            return (self.prepare_error(HostedPayment.Order.Order, 
                                       "400", 
                                       err_msg))
        FULL_URL = self._prepare_uri(self._ORDER_PATH + \
                                     self._URI_SEPARATOR + \
                                     order_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST", 
                                                url=FULL_URL, 
                                                data=data)
        return (self._process_response(response, HostedPayment.Order.Order))

    
    '''
    Process a rebill using Profile Id
    
    @param: Order object
    @return: Order object
    @raise: IOException
    @raise: OptimalException
    '''    
    def process_rebill_using_profile_id(self, data):
        FULL_URL = self._prepare_uri(self._ORDER_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST", 
                                                url=FULL_URL, 
                                                data=data)
        return (self._process_response(response, HostedPayment.Order.Order))
    
