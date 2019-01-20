#!/usr/bin/env python
# -*- coding: utf-8 -*-

from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest
from HTTPClient import NVPair
import simplejson as json

from datetime import timedelta
from datetime import datetime
import calendar
import uuid
import random

host = "http://10.12.47.60:8181"

customerRelationProfileUrl = '/service/de/product/customer-relation-profile'
productUrl = '/service/de/product/product'
PostDepositUrl = '/service/de/deposit/deposit/1/100000'
getDepositUrl = '/service/de/deposit/deposit'
depositCustomerRelationUrl = '/service/de/deposit/deposit-customer-relation'
platformUrl = '/service/de/product/platform'
cifRealCustomerUrl = '/service/cif/real-customer'
depositInvoiceUrl = '/service/de/deposit/deposit/invoice'
depositTransferPaymentUrl = '/service/de/deposit/deposit/transfer-payment'
#---------------------------------------------------------------------
customerRelationProfileCode = 1967412
productCode = 1
depositCode = 1790335
depositCustomerRelationCode = 1716494
platformCode = 1716674
cifRealCustomerCode = 6909936
depositInvoiceCode = 6814812
#---------------------------------------------------------------------
depositCustomerRelationDepositDtoId = 1790335




class UserBehavior :
    headers = [
        NVPair('Content-Type', 'application/json'),
        NVPair('Charset', 'UTF-8'),
    ]

    testNumber = 0

    def createRequest(self, description):
        self.testNumber += 1

        request = HTTPRequest(url=host)
        request.headers = self.headers
        Test(self.testNumber, description).record(request, HTTPRequest.getHttpMethodFilter())
        return request


    #----get------------------------------------------------------------
    def createGetRequest(self):
        self.depositRequest_get = self.createRequest("deposit request(GET)")
        self.depositInvoiceRequest_get = self.createRequest("deposit Invoice request(GET)")
        self.depositCustomerRelationRequest_get = self.createRequest("deposit Customer Relation request(GET)")
        self.cifRealCustomerRequest_get = self.createRequest("cif Real Customer request(GET)")
        self.platformRequest_get = self.createRequest("platform request(GET)")
        self.customerRelationProfileRequest_get = self.createRequest("customer Relation Profile request(GET)")
        self.productRequest_get = self.createRequest("product request(GET)")

    #--------------------
    def getRequest(self):
        self.depositInvoice_get()
        self.cifRealCustomer_get()
        self.deposit_customer_relation_get()
        self.platform_get()
        self.deposit_get()
        self.customer_relation_profile_get()
        self.product_get()

    #----post------------------------------------------------------------
    def createPostRequest(self):
        self.depositTransferPaymenttRequest_post = self.createRequest("deposit Transfer Payment request(POST)")
        self.cifRealCustomerRequest_post = self.createRequest("cif Real Customer request(POST)")
        self.platformRequest_post = self.createRequest("platform request(POST)")
        self.depositCustomerRelationRequest_post = self.createRequest("deposit Customer Relation request(POST)")
        self.depositRequest_post = self.createRequest("deposit request(POST)")
        self.customerRelationProfileRequest_post = self.createRequest("customer Relation Profile request(POST)")
        self.productRequest_post = self.createRequest("product request(POST)")

    #--------------------
    def postRequest(self):
        self.depositTransferPayment_post()
        self.cifRealCustomer_post()
        self.platform_post()
        self.deposit_customer_relation_post()
        self.deposit_post()
        self.customer_relation_profile_post()
        self.product_post()



    def call(self):
        self.createGetRequest()
        self.createPostRequest()

        self.getRequest()
        self.postRequest()



    # def on_start(self):
    #     """ on_start is called when a Locust start before any task is scheduled """
    #     self.login()
    #
    # def on_stop(self):
    #     """ on_stop is called when the TaskSet is stopping """
    #     self.logout()
    #
    # def login(self):
    #     pass
    #
    # def logout(self):
    #     pass
#------------------------------------------------------------------
    # def post(self, url, payload):
    #     return self.request.POST(url, JSONObject(payload), self.headers)#(url, data=json.dumps(payload), headers=self.headers)
    #
    # def get(self, url):
    #     # return self.client.get(url, headers=self.headers)
    #     return self.request.GET(url)
#-----------------------------------------------------------------
    def fakeDate(self):
        dt = datetime.now() + timedelta(days=1)
        unixTimestamp = calendar.timegm(dt.utctimetuple())

        return str(unixTimestamp) + '000'

    def fakeTitle(self):
        return uuid.uuid4().hex

    def addCode(self, url, code):
        return url + '/' + str(code)
#---get------------------------------------------------------------------------------------------

    def depositInvoice_get(self):
        self.depositInvoiceRequest_get.GET(self.addCode(depositInvoiceUrl, depositInvoiceCode))

    def cifRealCustomer_get(self):
        self.cifRealCustomerRequest_get.GET(self.addCode(cifRealCustomerUrl, cifRealCustomerCode))

    def deposit_customer_relation_get(self):
        self.depositCustomerRelationRequest_get.GET(self.addCode(depositCustomerRelationUrl, depositCustomerRelationCode))

    def platform_get(self):
        self.platformRequest_get.GET(self.addCode(platformUrl, platformCode))

    def deposit_get(self):
        self.depositRequest_get.GET(self.addCode(getDepositUrl, depositCode))

    def customer_relation_profile_get(self):
        self.customerRelationProfileRequest_get.GET(self.addCode(customerRelationProfileUrl, customerRelationProfileCode))

    def product_get(self):
        self.productRequest_get.GET(self.addCode(productUrl, productCode))
#----post---------------------------------------------------------------------------------------------
    def depositTransferPayment_post(self):
        payload = {
            "sourceDepositCode": random.randint(10, 1000010),
            "destinationDepositCode": random.randint(1000011, 2000010),
            "amount": "1"
        }

        self.depositTransferPaymenttRequest_post.POST(depositTransferPaymentUrl, json.dumps(payload))

    def cifRealCustomer_post(self):
        payload = {
            "id": None,
            "version": None,
            "customerType": "1",
            "foreignerCode": None,
            "nationalCode": 2300588951,
            "shahabCode": None,
            "shahabCodeConfirmed": None,
            "name": "شش",
            "lastName": "سس",
            "unifiedName": "شش*سس",
            "latinName": "Saman",
            "latinLastName": "Alishiri",
            "latinUnifiedName": "Saman*Alishiri",
            "nationalityId": 3883,
            "creditCode": None,
            "stockCode": None,
            "economicCode": None,
            "branchCode": 11,
            "enabled": 1,
            "disabledDate": None,
            "status": 1,
            "birthDate": 583273800000,
            "deathDate": None,
            "registerDate": 583273800000,
            "postalCode": None,
            "postalAddress": None,
            "fatherName": "حسن",
            "sex": "1",
            "idNumber": None,
            "seri": None,
            "serialNo": None,
            "originalId": None,
            "idIssueArea": None,
            "idIssueDate": None,
            "idDescription": None,
            "idIssuePlace": None,
            "birthPlaceId": None,
            "eCard": None,
            "maritalStatus": None,
            "childrenNumber": None,
            "healthStatus": None,
            "religionId": None,
            "ismId": None,
            "degreeId": None,
            "residentialStatus": None,
            "foreignerCertTypeId": None,
            "foreignerCert": None,
            "foreignerCertValidDate": None,
            "grandFather": None,
            "languageId": None,
            "maskanBankEmployee": None,
            "jobOwnershipTypeId": None,
            "jobGroupId": None,
            "jobSubgroupId": None,
            "activityField": None,
            "jobCompanyName": None,
            "personnelCode": None
        }

        self.cifRealCustomerRequest_post.POST(cifRealCustomerUrl,  json.dumps(payload))

    def platform_post(self):
        payload = {
            "code": "1",
            "title": self.fakeTitle(),
            "isProfitable": False,
            "hasDepositCertificate": False,
            "hasRolloverSettlement": True,
            "hasCheque": False,
            "hasWarrantyLending": False,
            "hasTermDuration": False,
            "hasDraw": True,
            "hasPrioritySecurities": False,
            "version": None,
            "maxOpenedDeposit": 1000
        }

        self.platformRequest_post.POST(platformUrl, json.dumps(payload))

    def deposit_customer_relation_post(self):
        payload = {
            "customerId": 1,
            "relationTypeId": 1,
            "percentShare": 1,
            "customerPhoneId": 1,
            "customerLetterId": 1,
            "relationStartDate": 1526067000000,
            "relationEndDate": 1526844600000,
            "depositDto": {
                "id": depositCustomerRelationDepositDtoId,
                "depositCode": "44292",
                "mainAccountId": None,
                "iban": None,
                "currency": None,
                "openOrganizationId": None,
                "platformId": None,
                "productId": None,
                "openDate": None,
                "openAmount": None,
                "customerType": None,
                "title": None,
                "efectiveDate": None,
                "closeDate": None,
                "closeReason": None,
                "hasCard": None,
                "hasDepositCertificate": None,
                "minAmount": None,
                "maxAmount": None,
                "mustSettle": None,
                "description": None,
                "minOpenAmount": None,
                "startTermDate": None,
                "endTermDate": None,
                "termRatio": None,
                "timeUnit": None,
                "settleAccountId": None,
                "sweepAccountId": None,
                "openerCustomerCode": None,
                "openerRelationType": None,
                "openerLetter": None,
                "version": None
            }
        }
        self.depositCustomerRelationRequest_post.POST(depositCustomerRelationUrl, json.dumps(payload))

    def deposit_post(self):
        payload = {
            "depositCode": None,
            "mainAccountId": None,
            "iban": None,
            "currency": None,
            "openOrganizationId": None,
            "platformId": None,
            "productId": 1,
            "openDate": None,
            "openAmount": 1,
            "customerType": None,
            "title": None,
            "efectiveDate": None,
            "closeDate": None,
            "closeReason": None,
            "hasCard": None,
            "hasDepositCertificate": None,
            "minAmount": None,
            "maxAmount": None,
            "mustSettle": None,
            "description": None,
            "minOpenAmount": None,
            "startTermDate": None,
            "endTermDate": None,
            "termRatio": None,
            "timeUnit": None,
            "settleAccountId": None,
            "sweepAccountId": None,
            "openerCustomerCode": None,
            "openerRelationType": None,
            "openerLetter": None,
            "version": None
        }
        self.depositRequest_post.POST(PostDepositUrl, json.dumps(payload))

    def customer_relation_profile_post(self):
        payload = {
            "code": "1",
            "title": self.fakeTitle(),
            "effectiveDate": self.fakeDate(),
            "personTypeProfileId": None,
            "personTypeProfileTitle": None,
            "nationalityProfileId": None,
            "residencyId": 10475,
            "minOpenerAge": 18,
            "ownerGenderProfileId": None,
            "minOwnerAge": 18,
            "minSignerAge": 18,
            "allowedOpenerProfileId": None,
            "legalPersonTypeProfileId": None,
            "legalPersonOwnerTypeProfileId": None
        }

        self.customerRelationProfileRequest_post.POST(customerRelationProfileUrl, json.dumps(payload))

    def product_post(self):
        payload = {
            "persianName": self.fakeTitle(),
            "englishName": self.fakeTitle(),
            "major": 1,
            "currency": "IRR",
            "platform": {
                "id": 642
            },
            "status": "OPENING",
            "effectiveDate": 1526153400000,
            "deactiveDate": 29927388600000,
            "customerRelationProfileDto": {
                "id": 661
            },
            "hasTermDuration": False,
            "termUnit": None,
            "minTermDuration": None,
            "maxTermDuration": None,
            "hasWarrantyLending": False,
            "minScoreAmount": 0,
            "hasDepositCertificate": False,
            "hasPassBook": True,
            "hasCheque": False,
            "hasBackup": False,
            "hasCard": True,
            "openingLocation": "BRANCH",
            "hasDormancy": False,
            "dormancyDuration": None,
            "minDormancyAmount": None,
            "minOpeningAmount": 0,
            "minBalanceAmount": 0,
            "stampDutyAmount": None,
            "hasGroupOpening": True,
            "hasDraw": True,
            "sedimentAmount": None,
            "hasAmlControl": True,
            "profitProfileId": None,
            "profitMethod": None,
            "profitRateProfile": None,
            "breakageProfileId": None,
            "hasPrioritySecurities": False,
            "hasDefenitiveProfit": False,
            "minAlertAmount": 10000,
            "hasInquiry": True,
            "depositTerm": None,
            "sendSms": True,
            "maxSharedDeposit": 100,
            "maxSingleDeposit": 1000,
            "stampDutyMethod": None,
            "statusDate": 1526153400000,
            "dormancyDurationUnit": None,
            "minDurationForNotDemanded": None,
            "unitForNotDemanded": None,
            "majorForStampDutyAmount": None,
            "hasIntroducer": False,
            "hasSediment": False,
            "hasTransferability": False,
            "backup": True,
            "profitable": False,
            "rollOverProfileId": None
        }

        self.productRequest_post.POST(productUrl, json.dumps(payload))


class TestRunner:
    def __call__(self):
        userBehavior = UserBehavior()
        userBehavior.call()


