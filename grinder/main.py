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


host = "http://10.12.47.73:8282"

loginUrl = '/service/platform/authentication/login'
refreshTokenUrl = '/service/platform/authentication/refresh'

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

testNumber = 0

headers = [
    NVPair('Content-Type', 'application/json'),
    NVPair('Charset', 'UTF-8'),
]

refreshTokenInterval = 1 #minuts


def log(message):
    grinder.logger.info(message)

def pickUpToken(response):
    return "JWT " + json.loads(response.getText())["payload"]["content"]["token"]

def calculateRefreshTokenTime(now):
    return now + timedelta(minutes=refreshTokenInterval)

def createRequest(description):
    global testNumber
    global headers

    testNumber += 1
    request = HTTPRequest(url=host)
    request.headers = headers
    Test(testNumber, description).record(request)
    return request


#----get------------------------------------------------------------
depositRequest_get = createRequest("deposit request(GET)")
depositInvoiceRequest_get = createRequest("deposit Invoice request(GET)")
depositCustomerRelationRequest_get = createRequest("deposit Customer Relation request(GET)")
cifRealCustomerRequest_get = createRequest("cif Real Customer request(GET)")
platformRequest_get = createRequest("platform request(GET)")
customerRelationProfileRequest_get = createRequest("customer Relation Profile request(GET)")
productRequest_get = createRequest("product request(GET)")

#----TokenRequest------------------------------------------------------------
loginRequest_post = createRequest("login request(POST)")
refreshTokenRequest_get = createRequest("refreshToken request(GET)")

#----post------------------------------------------------------------
depositTransferPaymenttRequest_post = createRequest("deposit Transfer Payment request(POST)")
cifRealCustomerRequest_post = createRequest("cif Real Customer request(POST)")
platformRequest_post = createRequest("platform request(POST)")
depositCustomerRelationRequest_post = createRequest("deposit Customer Relation request(POST)")
depositRequest_post = createRequest("deposit request(POST)")
customerRelationProfileRequest_post = createRequest("customer Relation Profile request(POST)")
productRequest_post = createRequest("product request(POST)")




class TestRunner:
    token = None

    headers = None

    totalTestCount = 15

    testCounter = 1

    refreshTime = None


    def refreshTokenDecider(self):
        now = datetime.now()
        if now >= self.refreshTime:
            self.refreshToken_get(now)

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
        depositInvoiceRequest_get.GET(self.addCode(depositInvoiceUrl, depositInvoiceCode),None, self.headers)

    def cifRealCustomer_get(self):
        cifRealCustomerRequest_get.GET(self.addCode(cifRealCustomerUrl, cifRealCustomerCode), None, self.headers)

    def deposit_customer_relation_get(self):
        depositCustomerRelationRequest_get.GET(self.addCode(depositCustomerRelationUrl, depositCustomerRelationCode), None, self.headers)

    def platform_get(self):
        platformRequest_get.GET(self.addCode(platformUrl, platformCode), None, self.headers)

    def deposit_get(self):
        depositRequest_get.GET(self.addCode(getDepositUrl, depositCode), None, self.headers)

    def customer_relation_profile_get(self):
        customerRelationProfileRequest_get.GET(self.addCode(customerRelationProfileUrl, customerRelationProfileCode), None, self.headers)

    def product_get(self):
        productRequest_get.GET(self.addCode(productUrl, productCode), None, self.headers)

    #----Token---------------------------------------------------------------------------------------------
    def refreshToken_get(self, now):
        self.refreshTime = calculateRefreshTokenTime(now)
        response = refreshTokenRequest_get.GET(refreshTokenUrl, None, self.headers)
        self.token = pickUpToken(response)

    def login_post(self, payload):
        return loginRequest_post.POST(loginUrl, json.dumps(payload))

    #----post---------------------------------------------------------------------------------------------
    def depositTransferPayment_post(self):
        payload = {
            "sourceDepositCode": random.randint(10, 1000010),
            "destinationDepositCode": random.randint(1000011, 2000010),
            "amount": "1"
        }

        depositTransferPaymenttRequest_post.POST(depositTransferPaymentUrl, json.dumps(payload), self.headers)

    def cifRealCustomer_post(self):
        payload = {
            "id": None,
            "version": None,
            "customerType": "1",
            "foreignerCode": None,
            "nationalCode": 2300588951,
            "shahabCode": None,
            "shahabCodeConfirmed": None,
            "name": "hasan",
            "lastName": "taghavi",
            "unifiedName": "unali",
            "latinName": "Saman",
            "latinLastName": "Alaki",
            "latinUnifiedName": "Saman*Alaki",
            "nationalityId": 3883,
            "creditCode": None,
            # "stockCode": None,
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
            "fatherName": "TAGHI",
            "sex": "1",
            "idNumber": None,
            "seri": None,
            "serialNo": None,
            "originalId": None,
            "idIssueArea": None,
            "idIssueDate": None,
            "idDescription": None,
            "idIssuePlace": 1,
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

        cifRealCustomerRequest_post.POST(cifRealCustomerUrl,  json.dumps(payload), self.headers)

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

        platformRequest_post.POST(platformUrl, json.dumps(payload), self.headers)

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

        depositCustomerRelationRequest_post.POST(depositCustomerRelationUrl, json.dumps(payload), self.headers)

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

        depositRequest_post.POST(PostDepositUrl, json.dumps(payload), self.headers)

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

        customerRelationProfileRequest_post.POST(customerRelationProfileUrl, json.dumps(payload), self.headers)

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

        productRequest_post.POST(productUrl, json.dumps(payload), self.headers)

    def __init__(self):
        payload = {
            "username": "test",
            "password": "1234"
        }

        self.refreshTime = calculateRefreshTokenTime(datetime.now())

        response = self.login_post(payload)
        self.token = pickUpToken(response)
        # print self.token
        # log(self.token)
        # log("initialising")



    def __call__(self):
        self.headers = [
            NVPair('Content-Type', 'application/json'),
            NVPair('Charset', 'UTF-8'),
            NVPair('Authorization', self.token)
        ]

        if self.testCounter == 1:
            self.depositInvoice_get()
        elif self.testCounter == 2:
            self.cifRealCustomer_get()
        elif self.testCounter == 3:
            self.deposit_customer_relation_get()
        elif self.testCounter == 4:
            self.platform_get()
        elif self.testCounter == 5:
            self.deposit_get()
        elif self.testCounter == 6:
            self.customer_relation_profile_get()
        elif self.testCounter == 7:
            self.product_get()
        elif self.testCounter == 8:
            self.depositTransferPayment_post()
        elif self.testCounter == 9:
            self.cifRealCustomer_post()
        elif self.testCounter == 10:
            self.platform_post()
        elif self.testCounter == 11:
            self.deposit_customer_relation_post()
        elif self.testCounter == 12:
            self.deposit_post()
        elif self.testCounter == 13:
            self.customer_relation_profile_post()
        elif self.testCounter == 14:
            self.product_post()
        elif self.testCounter == 15:
            self.refreshTokenDecider()

        if self.testCounter >= self.totalTestCount:
            self.testCounter = 1
        else:
            self.testCounter += 1


            # log(self.token)
            #log("in __call__()")



