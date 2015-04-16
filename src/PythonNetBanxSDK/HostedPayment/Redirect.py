'''
Created on 05-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.common.DomainObject import DomainObject


class Redirect(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['rel'] = self.rel
        handler['returnKeys'] = self.returnKeys
        handler['uri'] = self.uri
        handler['delimiter'] = self.delimiter
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
        
    '''
    Property Rel
    '''   
    def rel(self, rel):
        self.__dict__['rel'] = rel
        
    '''
    Property Return Keys
    '''   
    def returnKeys(self, return_keys):
        self.__dict__['returnKeys'] = return_keys
        
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
