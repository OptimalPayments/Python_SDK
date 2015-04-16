'''
Created on 19-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.common.DomainObject import DomainObject


class Callback(DomainObject):
    '''
    classdocs
    '''
    def __init__(self,obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['format'] = self.format
        handler['rel'] = self.rel
        handler['retries'] = self.retries
        handler['returnKeys'] = self.returnKeys
        handler['synchronous'] = self.synchronous
        handler['uri'] = self.uri
        handler['delimiter'] = self.delimiter
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
                
    '''
    Property Format
    '''   
    def format(self, format_):
        self.__dict__['format'] = format_
        
    '''
    Property Rel
    '''   
    def rel(self, rel):
        self.__dict__['rel'] = rel
        
    '''
    Property Retries
    '''   
    def retries(self, retries):
        self.__dict__['retries'] = retries
        
    '''
    Property Return Keys
    '''   
    def returnKeys(self, return_keys):
        self.__dict__['returnKeys'] = return_keys
        
    '''
    Property Synchronous
    '''   
    def synchronous(self, synchronous):
        self.__dict__['synchronous'] = synchronous
    
    '''
    Property Uri
    '''   
    def uri(self, uri):
        self.__dict__['uri'] = uri
        
    '''
    Property Delimiter
    '''   
    def delimiter(self, delimiter):
        self.__dict__['delimiter'] = delimiter
        
    '''
    Property Status
    '''
    def status(self, status):
        self.__dict__['status'] = status

        