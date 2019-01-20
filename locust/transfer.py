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

#----post---------------------------------------------------------------------------------------------
    @task
    def depositTransferPayment_post(self):
        self.post(depositTransferPaymentUrl, None)

    


class WebsiteUser(HttpLocust):
    # locust.stats.CSV_STATS_INTERVAL_SEC = 5 # default is 2 seconds
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
    stop_timeout = 10000
    #host = "http://10.12.47.60:8181"