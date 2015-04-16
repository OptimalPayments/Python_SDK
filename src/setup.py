'''
Created on 10-Feb-2015

@author: Siva.Reddy
'''
from setuptools import setup

setup(
    name='OptimalPayment',
    version=2.0,

    author='Opus Software Solutions Pvt. Ltd.',
    author_email='deepak.agarwal@opussoft.com',
    description=('This document provides the release details of the Python SDK for NETBANX API' ),
    license='Opus Software Solutions Pvt. Ltd.',
    packages=["bin","PythonNetBanxSDK","PythonNetBanxSDK/CardPayments","PythonNetBanxSDK/CustomerVault","PythonNetBanxSDK/HostedPayment","PythonNetBanxSDK/common"],
    include_package_data=True,
    zip_safe=False,
    py_modules = ['PythonNetBanxSDK','HTMLTestRunner','bin'],     
)
