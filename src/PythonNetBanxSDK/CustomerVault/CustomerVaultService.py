'''
Created on 30-Jan-2015

@author: Asawari.Vaidya
'''
import inspect
from PythonNetBanxSDK import CustomerVault
from PythonNetBanxSDK import common


class CustomerVaultService(object):
    '''
    classdocs
    '''
    # Define URL paths for Customer Profile, Address and Card
    _MONITOR_PATH = '/customervault/monitor'
    _URI = '/customervault/v1'
    _PROFILE_PATH = '/profiles/'
    _ADDRESS_PATH = '/addresses/'
    _CARD_PATH = '/cards/'
 
    def __init__(self, optimal_object):
        '''
        Constructor
        '''
        self.optimal_object = optimal_object
           
    '''
    Prepare URL for process request
    @param: Chunks of paths
    @return: Complete URL for Processing Request
    '''
    def _prepare_uri(self, path):
        return self._URI + path
    
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
            return self.prepare_error(class_name, response.code, 
                                                  response.message)
        else:
            return (class_name(response))
    
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
        return (self._process_response(response, CustomerVault.Profile.Profile))
    
    '''
    Create a Customer Profile
    
    @param: Profile object
    @return: Profile object
    @raise: IOException
    @raise: OptimalException
    '''
    def create_profile(self, data):
        FULL_URL = self._prepare_uri(self._PROFILE_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST",
                                                url=FULL_URL,
                                                data=data)   
        return (self._process_response(response, CustomerVault.Profile.Profile))
    
    '''
    Lookup a Customer Profile
    
    @param: Profile Id
    @return: Profile object
    @raise exception: IOException
    @raise exception: OptimalException
    '''
    def lookup_profile(self, data):
        profile_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                     profile_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)                
        return (self._process_response(response, CustomerVault.Profile.Profile))

    '''
    Lookup a Customer Profile with Subcomponents
    
    @param: Profile Id
    @param: is_ddresses indicate whether to include addresses in response
    @param: is_ards indicate whether to include cards in response 
    @return: Profile object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_profile_subcomponents(self, data, is_addresses, is_cards):
        _subcomponents = '?fields=cards,addresses'
        _subcomponent_card = '?fields=cards'
        _subcomponent_address = '?fields=addresses'
        
        profile_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg))
        del data.id

        if (is_addresses is True and is_cards is True):
            FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                         profile_id + \
                                         _subcomponents)
        elif (is_addresses is True and is_cards is False):
            FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                         profile_id + \
                                         _subcomponent_address)
        elif (is_addresses is False and is_cards is True):
            FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                         profile_id + \
                                         _subcomponent_card)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)  
        return (self._process_response(response, CustomerVault.Profile.Profile))           
    
    '''
    Update a Customer Profile
    
    @param: Profile Id, Profile object
    @return: Profile object
    @raise: IOException
    @raise: OptimalException
    '''
    def update_profile(self, data):
        profile_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg))
        del data.id
         
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                     profile_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response, CustomerVault.Profile.Profile))
    
    '''
    Delete a Customer Profile
    
    @param: Profile Id
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    def delete_profile(self, data):
        profile_id = data.id
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                     profile_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None)   
        return (self._process_response(response, CustomerVault.Profile.Profile))
     
    '''
    Create an Address
    
    @param: Profile Id, Address object
    @return: Address object
    @raise: IOException
    @raise: OptimalException
    '''
    def create_address(self, data):
        profile_id = data.profile.id 
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg))   
        del data.profile

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                     profile_id + \
                                     self._ADDRESS_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response, 
                                       CustomerVault.Addresses.Address))
        
    '''
    Lookup an Address
    
    @params: Profile Id, Address Id, Address object
    @return: Address object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_address(self, data):
        profile_id = data.profile.id    
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(
                                    CustomerVault.Addresses.Address, 
                                    "400", 
                                    err_msg))
        del data.profile
        address_id = data.id
        if inspect.ismethod(address_id):
            err_msg = "Address Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg))
        del data.id
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                     profile_id + \
                                     self._ADDRESS_PATH + \
                                     address_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)      
        return (self._process_response(response, 
                                       CustomerVault.Addresses.Address))
    
    '''
    Update an Address
    
    @param: Profile Id, Address Id, Address object
    @return: Address object
    @raise: IOException
    @raise: OptimalException
    '''
    def update_address(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg)) 
        del data.profile
        address_id = data.id
        if inspect.ismethod(address_id):
            err_msg = "Address Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                     profile_id + \
                                     self._ADDRESS_PATH + \
                                     address_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)        
        return (self._process_response(response, 
                                       CustomerVault.Addresses.Address))
     
    '''
    Delete an Address
    
    @param: Profile Id, Address Id
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    def delete_address(self, data):
        profile_id = data.profile.id 
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg))       
        del data.profile
        address_id = data.id
        if inspect.ismethod(address_id):
            err_msg = "Address Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg)) 
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                     profile_id + \
                                     self._ADDRESS_PATH + \
                                     address_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None)
        return (self._process_response(response, 
                                       CustomerVault.Addresses.Address))
     
    '''
    Create a Card
    
    @param: Profile Id, Card object
    @return: Card object
    @raise: IOException
    @raise: OptimalException
    '''
    def create_card(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg))  
        del data.profile
        
        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                     profile_id + \
                                     self._CARD_PATH)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="POST", 
                                                url=FULL_URL, 
                                                data=data)    
        return (self._process_response(response, 
                                       CustomerVault.Card.Card))
    
    '''
    Lookup a Card
    
    @param: Profile Id, Card Id, Card object
    @return: Card object
    @raise: IOException
    @raise: OptimalException
    '''
    def lookup_card(self, data):
        profile_id = data.profile.id 
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg))      
        del data.profile
        card_id = data.id
        if inspect.ismethod(card_id):
            err_msg = "Card Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                     profile_id + \
                                     self._CARD_PATH + \
                                     card_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="GET", 
                                                url=FULL_URL, 
                                                data=None)     
        return (self._process_response(response, 
                                       CustomerVault.Card.Card))
    
    '''
    Update a Card
    
    @param: Profile Id, Card Id, Card object
    @return: Card object
    @raise: IOException
    @raise: OptimalException
    '''
    def update_card(self, data):
        profile_id = data.profile.id   
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg))       
        del data.profile
        card_id = data.id
        if inspect.ismethod(card_id):
            err_msg = "Card Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg))   
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                     profile_id + \
                                     self._CARD_PATH + \
                                     card_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="PUT", 
                                                url=FULL_URL, 
                                                data=data)      
        return (self._process_response(response,
                                       CustomerVault.Card.Card))
    
    '''
    Delete a Card
    
    @param: Profile Id, Card Id
    @return: Response Status
    @raise: IOException
    @raise: OptimalException
    '''
    def delete_card(self, data):
        profile_id = data.profile.id  
        if inspect.ismethod(profile_id):
            err_msg = "Profile Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg))         
        del data.profile
        card_id = data.id
        if inspect.ismethod(card_id):
            err_msg = "Card Id not available"
            return (self.prepare_error(CustomerVault.Addresses.Address, 
                                       "400", 
                                       err_msg))
        del data.id

        FULL_URL = self._prepare_uri(self._PROFILE_PATH + \
                                     profile_id + \
                                     self._CARD_PATH + \
                                     card_id)
        # print ("Communicating to ", FULL_URL)
        response = self.optimal_object.process_request(
                                                req_method="DELETE", 
                                                url=FULL_URL, 
                                                data=None) 
        return (self._process_response(response, 
                                       CustomerVault.Card.Card))