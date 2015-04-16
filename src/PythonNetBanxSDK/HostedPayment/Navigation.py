'''
Created on 19-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.common.DomainObject import DomainObject


class Navigation(DomainObject):
    '''
    classdocs
    '''
    def __init__(self,obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['prev'] = self.prev
        handler['next'] = self.next
        
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
                
    '''
    Property Prev
    '''   
    def prev(self, prev):
        self.__dict__['prev'] = prev
        
    '''
    Property Next
    '''   
    def next(self, next_):
        self.__dict__['next'] = next_
