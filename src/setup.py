'''
Created on 10-Feb-2015

@author: Siva.Reddy
'''
from setuptools import setup


setup(
    name='OptimalPayment',
    version=2.1,

    author='Opus Consulting Solutions Pvt. Ltd.',
    author_email='deepak.agarwal@opusconsulting.com',
    description=('This document provides the release details of the Python SDK for NETBANX API' ),
    license='Opus Consulting Solutions Pvt. Ltd.',
    packages=["utils","bin","PythonNetBanxSDK","PythonNetBanxSDK/CardPayments","PythonNetBanxSDK/CustomerVault","PythonNetBanxSDK/HostedPayment","PythonNetBanxSDK/common", "PythonNetBanxSDK/DirectDebit", "PythonNetBanxSDK/ThreeDSecure"],
    include_package_data=True,
    zip_safe=False,
    py_modules = ['PythonNetBanxSDK','HTMLTestRunner','bin','utils'],     
)
