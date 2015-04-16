'''
Created on 04-Feb-2015

@author: Asawari.Vaidya
'''
from PythonNetBanxSDK.HostedPayment.ShoppingCart import ShoppingCart
from PythonNetBanxSDK.HostedPayment.AncillaryFee import AncillaryFee
from PythonNetBanxSDK.CardPayments.BillingDetails import BillingDetails
from PythonNetBanxSDK.CardPayments.ShippingDetails import ShippingDetails
from PythonNetBanxSDK.HostedPayment.Redirect import Redirect
from PythonNetBanxSDK.HostedPayment.ExtendedOptions import ExtendedOptions
from PythonNetBanxSDK.HostedPayment.AddendumData import AddendumData
from PythonNetBanxSDK.HostedPayment.AssociatedTransactions import \
                                    AssociatedTransactions
from PythonNetBanxSDK import CustomerVault
from PythonNetBanxSDK import common
from PythonNetBanxSDK.HostedPayment.Transaction import Transaction
from PythonNetBanxSDK.common.DomainObject import DomainObject
from PythonNetBanxSDK.common.Link import Link


class Order(DomainObject):
    '''
    classdocs
    '''
    def __init__(self, obj):
        '''
        Constructor
        '''
        # Handler dictionary
        handler = dict()
        handler['profile'] = self.profile
        handler['shoppingCart'] = self.shoppingCart
        handler['ancillaryFees'] = self.ancillaryFees
        handler['billingDetails'] = self.billingDetails
        handler['shippingDetails'] = self.shippingDetails
        handler['callback'] = self.callback
        handler['redirect'] = self.redirect
        handler['addendumData'] = self.addendumData
        handler['extendedOptions'] = self.extendedOptions
        handler['associatedTransactions'] = self.associatedTransactions
        handler['transaction'] = self.transaction
        handler['error'] = self.error
        handler['link'] = self.link
              
        if obj is not None:
            self.setProperties(obj, handler=handler)
        else:
            pass
                  
    '''
    Property Id
    '''   
    def id(self, id_):
        self.__dict__['id'] = id_

    '''
    Property Merchant Reference Number
    '''   
    def merchantRefNum(self, merchant_ref_num):
        self.__dict__['merchantRefNum'] = merchant_ref_num

    '''
    Property Currency Code
    '''   
    def currencyCode(self, currency_code):
        self.__dict__['currencyCode'] = currency_code

    '''
    Property Total Amount
    '''   
    def totalAmount(self, total):
        self.__dict__['totalAmount'] = total

    '''
    Property Customer Ip
    '''   
    def customerIp(self, customer_ip):
        self.__dict__['customerIp'] = customer_ip

    '''
    Property Customer Notification Email
    '''   
    def customerNotificationEmail(self, customer_notification_email):
        self.__dict__['customerNotificationEmail'] = customer_notification_email

    '''
    Property Merchant Notification Email
    '''   
    def merchantNotificationEmail(self, merchant_notification_email):
        self.__dict__['merchantNotificationEmail'] = merchant_notification_email

    '''
    Property Due Date
    '''   
    def dueDate(self, due_date):
        self.__dict__['dueDate'] = due_date

    '''
    Property Profile
    @param: Profile Object
    '''   
    def profile(self, profile):
        if isinstance(profile, CustomerVault.Profile.Profile):
            p = CustomerVault.Profile.Profile(profile.__dict__)
            self.__dict__['profile'] = p
        else:
            p = CustomerVault.Profile.Profile(profile)
            self.__dict__['profile'] = p

    '''
    Property ShoppingCart
    @param: ShoppingCart Object
    '''   
    def shoppingCart(self, shopping_cart):
        if isinstance(shopping_cart, ShoppingCart):
            sc = ShoppingCart(shopping_cart.__dict__)
            self.__dict__['shoppingCart'] = sc
        else:
            sc = ShoppingCart(shopping_cart)
            self.__dict__['shoppingCart'] = sc

    '''
    Property AncillaryFees
    @param: AncillaryFees Object
    '''   
    def ancillaryFees(self, ancillary_fees):
        if isinstance(ancillary_fees, AncillaryFee):
            af = AncillaryFee(ancillary_fees.__dict__)
            self.__dict__['ancillaryFees'] = af
        else:
            af = AncillaryFee(ancillary_fees)
            self.__dict__['ancillaryFees'] = af

    '''
    Property BillingDetails
    @param: BillingDetails Object
    '''   
    def billingDetails(self, billing_details):
        if isinstance(billing_details, BillingDetails):
            bd = BillingDetails(billing_details.__dict__)
            self.__dict__['billingDetails'] = bd
        else:
            bd = BillingDetails(billing_details)
            self.__dict__['billingDetails'] = bd

    '''
    Property ShippingDetails
    @param: ShippingDetails Object
    '''   
    def shippingDetails(self, shipping_details):
        if isinstance(shipping_details):
            sd = ShippingDetails(shipping_details.__dict__)
            self.__dict__['shippingDetails'] = sd
        else:    
            sd = ShippingDetails(shipping_details)
            self.__dict__['shippingDetails'] = sd

    '''
    Property Callback
    '''   
    def callback(self, callback):
        self.__dict__['callback'] = callback

    '''
    Property Redirect
    @param: Redirect Object
    '''   
    def redirect(self, redirect):
        if isinstance(redirect, Redirect):
            r = Redirect(redirect.__dict__)
            self.__dict__['redirect'] = r
        else:
            for count in range(0, redirect.__len__()):
                l = Redirect(redirect[count])
                self.__dict__.setdefault('redirect', []).append(l)

    '''
    Property Link
    @param: Link Object, List of Link Objects
    '''   
    def link(self, link):
        if isinstance(link, common.Link.Link):
            addr = common.Link.Link(link)
            self.__dict__['link'] = addr
        else:
            for count in range(0, link.__len__()):
                addr_obj = common.Link.Link(link[count])
                self.__dict__.setdefault('link', []).append(addr_obj)

    '''
    Property Mode
    '''   
    def mode(self, mode):
        self.__dict__['mode'] = mode

    '''
    Property Type
    '''   
    def type(self, type_):
        self.__dict__['type'] = type_

    '''
    Property Payment Method
    '''   
    def paymentToken(self, payment_token):
        self.__dict__['paymentToken'] = payment_token

    '''
    Property Addendum Data
    '''   
    def addendumData(self, addendum_data):
        if isinstance(addendum_data, AddendumData):
            ad = AddendumData(addendum_data.__dict__)
            self.__dict__['addendumData'] = ad
        else:
            ad = AddendumData(addendum_data)
            self.__dict__['addendumData'] = ad

    '''
    Property Locale
    '''   
    def locale(self, locale):
        self.__dict__['locale'] = locale

    '''
    Property Extended Options
    @param: ExtendedOptions Object
    @return: List of ExtendedOptions Object
    '''   
    def extendedOptions(self, extended_options):
        if isinstance(extended_options, ExtendedOptions):
            l = ExtendedOptions(extended_options)
            self.__dict__['extendedOptions'] = l
        else:
            for count in range(0, extended_options.__len__()):
                l = ExtendedOptions(extended_options[count])
                self.__dict__.setdefault('extendedOptions', []).append(l)

    '''
    Property Associated Transactions
    @param: AssociatedTransactinos Object
    '''   
    def associatedTransactions(self, associated_transactions):
        if isinstance(associated_transactions, AssociatedTransactions):
            at = AssociatedTransactions(associated_transactions.__dict__)
            self.__dict__['associatedTransactions'] = at
        else:
            at = AssociatedTransactions(associated_transactions)
            self.__dict__['associatedTransactions'] = at

    '''
    Property Transaction
    @param:  Transaction Object
    '''   
    def transaction(self, transaction):
        if isinstance(transaction, Transaction):
            at = Transaction(transaction.__dict__)
            self.__dict__['transaction'] = at        
        else:
            at = Transaction(transaction)
            self.__dict__['transaction'] = at

    '''
    Property Status
    '''   
    def status(self, status):
        self.__dict__['status'] = status

    '''
    Property Error
    @param: Error Object
    '''   
    def error(self, error):
        e = common.Error.Error(error)
        self.__dict__['error'] = e

    '''
    Property Links
    @param: Link Object, List of Link objects
    '''        
    def links(self, links):
        if isinstance(links, Link):
            l = Link(links)
            self.__dict__['links'] = l
        else:
            for count in range(0, links.__len__()):
                l = Link(links[count])
                self.__dict__.setdefault('links', []).append(l)