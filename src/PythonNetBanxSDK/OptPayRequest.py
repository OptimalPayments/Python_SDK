'''
Created on 16-Feb-2015

@author: Asawari.Vaidya
'''


class OptPayRequest(object):
    
    def __init__(self, api_end_point, api_url, method, query_string):
        '''
        Constructor
        '''
        self._api_end_point = api_end_point
        self._api_url = api_url
        self._method = method
        self._query_string = query_string

    '''
    Get Method
    '''
    def getMethod(self):
        return self._method

    '''
    Build URL
    @return: URL
    '''
    def buildUrl(self):
        return self._api_end_point + "/" + self._api_url
    
    '''
    Build URL Without Host
    @return: URL
    '''
    def buildUrlWithoutHost(self):
        return "/" + self._api_url