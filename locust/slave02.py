from threading import Lock, Thread

from locust import HttpLocust, TaskSet, task
import locust.stats

from datetime import timedelta
from datetime import datetime
import calendar
import uuid
import json
import random

lock = Lock()

day = 0

customerUrl = '/service/de/product/customer-relation-profile'
productUrl = '/service/de/product/product'
depositUrl = '/service/de/deposit/deposit'
depositRelationUrl = '/service/de/deposit/deposit-customer-relation'
platformUrl = '/service/de/product/platform'
cifUrl = '/service/cif/real-customer'


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
        # self.client.post("/login", {
        #  "username": "test_user",
        #  "password": ""
        # })

    def logout(self):
        pass

    def post(self, url, payload):
        return self.client.post(url, data=json.dumps(payload), headers=self.headers)

    def get(self, url):
        with self.client.get(url, headers=self.headers, catch_response=True) as response:
            if response.status_code == 500:
                response.success()

        # return self.client.get(url, headers=self.headers)

    def fakeDate(self):
        global day

        lock.acquire()
        day += 1
        lock.release()

        dt = datetime.now() + timedelta(days=day)
        unixTimestamp = calendar.timegm(dt.utctimetuple())

        return str(unixTimestamp) + '000'

    def fakeTitle(self):
        return uuid.uuid4().hex

    def fakeCode_small(self):
        return random.randint(1, 1000000)

    def fakeCode(self):
        global code

        lock.acquire()
        code = random.randint(200000, 1000000)
        lock.release()

        return code

    def addCodeCustomer(self, url):
        code = random.randint(1, 1000000)
        return url + '/' + str(code)
    def addCodeProduct(self, url):
        code = random.randint(1, 1000000)
        return url + '/' + str(code)
    def addCodeDeposit(self, url):
        code = random.randint(1, 1000000)
        return url + '/' + str(code)
    def addCodeDepositRelation(self, url):
        code = random.randint(1, 1000000)
        return url + '/' + str(code)
    def addCodePlatform(self, url):
        code = random.randint(1, 1000000)
        return url + '/' + str(code)
    def addCodeCif(self, url):
        code = random.randint(1, 1000000)
        return url + '/' + str(code)

    #@task
    def cif_get(self):
        self.get(self.addCodeCif(cifUrl))

    @task
    def cif_relation_post(self):
        payload = {
                   "customerNumber": self.fakeCode(),
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

        self.post(cifUrl, payload)

    #@task
    def platform_get(self):
        self.get(self.addCodePlatform(platformUrl))

    @task
    def platform_post(self):
        payload = {
            "code": self.fakeCode(),
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

    #@task
    def deposit_relation_get(self):
        self.get(self.addCodeDepositRelation(depositRelationUrl))

    @task
    def deposit_relation_post(self):
        payload = {
            "customerId": 1,
            "relationTypeId": 1,
            "percentShare": 1,
            "customerPhoneId": 1,
            "customerLetterId": 1,
            "relationStartDate": 1526067000000,
            "relationEndDate": 1526844600000,
            "depositDto": {
                "id": 250,
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
        self.post(depositRelationUrl, payload)

    #@task
    def deposit_get(self):
        self.get(self.addCodeDeposit(depositUrl))

    @task
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
        self.post(depositUrl, payload)

    #@task
    def customer_get(self):
        self.get(self.addCodeCustomer(customerUrl))

    @task
    def customer_post(self):
        code = self.fakeCode()
        payload = {
            "code": code,
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

        # print code

        self.post(customerUrl, payload)

    #@task
    def product_get(self):
        self.get(self.addCodeProduct(productUrl))

    @task
    def product_post(self):
        payload = {
            "code": self.fakeCode(),
            "persianName": self.fakeTitle(),
            "englishName": self.fakeTitle(),
            "major": 1,
            "currency": "IRR",
            "platform": {
                "id": 642,
                "code": 1,
                "title": "123213",
                "isProfitable": None,
                "hasDepositCertificate": None,
                "hasRolloverSettlement": None,
                "hasCheque": None,
                "hasWarrantyLending": None,
                "hasTermDuration": None,
                "hasDraw": None,
                "hasPrioritySecurities": None,
                "version": None,
                "maxOpenedDeposit": None
            },
            "status": "OPENING",
            "effectiveDate": self.fakeDate(),
            "deactiveDate": 29927388600000,
            "customerRelationProfileDto": {
                "id": 661,
                "code": 111,
                "title": "uuu",
                "effectiveDate": None,
                "personTypeProfileId": None,
                "personTypeProfileTitle": None,
                "nationalityProfileId": None,
                "residencyId": None,
                "minOpenerAge": None,
                "ownerGenderProfileId": None,
                "minOwnerAge": None,
                "minSignerAge": None,
                "allowedOpenerProfileId": None,
                "legalPersonTypeProfileId": None,
                "legalPersonOwnerTypeProfileId": None
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
            "operationGroupDto": {
                "id": None,
                "code": None,
                "title": "",
                "groupType": None,
                "version": None
            },
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
    min_wait = 5000
    max_wait = 9000
    stop_timeout = 10000
    #host = "http://10.12.47.60:8181"