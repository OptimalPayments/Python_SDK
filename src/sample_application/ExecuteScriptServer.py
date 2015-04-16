'''
Created on 1-Apr-2015

@author: Asawari.Vaidya
'''
#import os,sys
from http.server import HTTPServer, CGIHTTPRequestHandler

HOST = '127.0.0.1'
port = 3000

#os.chdir('/home/nehamehta/Asawari/PythonSDK/src/sample_application')

httpd = HTTPServer((HOST, port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))

CGIHTTPRequestHandler.cgi_directories=["/"]
#CGIHTTPRequestHandler.cgi_directories = ['/home/nehamehta/Asawari/PythonSDK/src/sample_application']
#sys.path.append("/")

httpd.serve_forever()	
