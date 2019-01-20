from locust import HttpLocust, TaskSet, task
# import locust.stats

from datetime import timedelta
from datetime import datetime
import calendar
import uuid
import json

customerRelationProfileUrl = '/service/de/product/customer-relation-profile'
productUrl = '/service/de/product/product'
PostDepositUrl = '/service/de/deposit/deposit/1/100000'
getDepositUrl = '/service/de/deposit/deposit'
depositCustomerRelationUrl = '/service/de/deposit/deposit-customer-relation'
platformUrl = '/service/de/product/platform'
cifRealCustomerUrl = '/service/cif/real-customer'
depositInvoiceUrl = '/service/de/deposit/deposit/invoice'
depositTransferPaymentUrl = '/service/de/deposit/deposit/transfer-payment/6814817/6814827/1'
#---------------------------------------------------------------------
customerRelationProfileCode = 1967412
productCode = 1
depositCode = 1790335
depositCustomerRelationCode = 1716494
platformCode = 1716674
cifRealCustomerCode = 1
depositInvoiceCode = 6814812
#---------------------------------------------------------------------


depositCustomerRelationDepositDtoId = 1790335

class UserBehavior(TaskSet):
    headers = {'content-type': 'application/json'}

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        pass

    def logout(self):
        pass
#------------------------------------------------------------------
    def post(self, url, payload):
        return self.client.post(url, data=json.dumps(payload), headers=self.headers)

    def get(self, url):
        return self.client.get(url, headers=self.headers)
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
    @task(100)
    def depositInvoice_get(self):
        self.get(self.addCode(depositInvoiceUrl, depositInvoiceCode))
    @task(100)
    def cifRealCustomer_get(self):
        self.get(self.addCode(cifRealCustomerUrl, cifRealCustomerCode))

    @task(5)
    def deposit_customer_relation_get(self):
        self.get(self.addCode(depositCustomerRelationUrl, depositCustomerRelationCode))

    @task(5)
    def platform_get(self):
        self.get(self.addCode(platformUrl, platformCode))

    @task(5)
    def deposit_get(self):
        self.get(self.addCode(getDepositUrl, depositCode))

    @task(5)
    def customer_relation_profile_get(self):
        self.get(self.addCode(customerRelationProfileUrl, customerRelationProfileCode))

    @task(5)
    def product_get(self):
        self.get(self.addCode(productUrl, productCode))
#----post---------------------------------------------------------------------------------------------
    @task(1000)
    def depositTransferPayment_post(self):
        self.post(depositTransferPaymentUrl, None)

    @task(100)
    def cifRealCustomer_post(self):
        payload = {
                   "customerNumber": "2",
                   "uniqueCode": "6662817712",
                   "name": "NAME_cfgSKFelbT225",
                   "lastName": "LAST_NAME_225ssZVGXPrji",
                   "unifiedName": "NAME225*LAST_NAME225",
                   "latinName": "LATIN_NAME_Czmsff225",
                   "latinLastName": "LATIN_LAST_NAME_Esvgfgwwonfbzfpwbqw225",
                   "latinUnifiedName": "LATIN_NAME225*LATIN_LAST_NAME225",
                   "customerTypeId": "3883",
                   "nationalityId": "98",
                   "fatherName": "fgfgggg",
                   "sex": 1,
                   "birthDate": None,
                   "originalCertificate": None,
                   "certificateNumber": None,
                   "seri": None,
                   "serialNo": None,
                   "certificateIssueArea": None,
                   "certificateIssueDate": None,
                   "certificateIssuePlace": None,
                   "birthPlace": None,
                   "hasElectronicNationalCard": None,
                   "maritalStatus": None,
                   "childrenNumber": None,
                   "degreeOfEducation": None,
                   "residentialStatus": None,
                   "foreignerCertificateType": None,
                   "foreignerCertificateNumber": None,
                   "foreignerCertificateValidityDate": None,
                   "foreignerGrandFather": None,
                   "foreignerLanguage": None,
                   "stockCode": None,
                   "occupationType": None,
                   "occupationGroup": None,
                   "occupationSubGroup": None,
                   "occupationTitle": None,
                   "personalNumber": None}

        self.post(cifRealCustomerUrl, payload)

    @task(5)
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

        self.post(platformUrl, payload)

    @task(5)
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
        self.post(depositCustomerRelationUrl, payload)

    @task(5)
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
        self.post(PostDepositUrl, payload)

    @task(5)
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

        self.post(customerRelationProfileUrl, payload)

    @task(5)
    def product_post(self):
        payload =  {
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


        self.post(productUrl, payload)


class WebsiteUser(HttpLocust):
    # locust.stats.CSV_STATS_INTERVAL_SEC = 5 # default is 2 seconds
    task_set = UserBehavior
    min_wait = 500
    max_wait = 1000
    stop_timeout = 10000
    #host = "http://10.12.47.60:8181"