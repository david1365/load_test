from locust import HttpLocust, TaskSet, task
# import locust.stats

from datetime import timedelta
from datetime import datetime
import calendar
import uuid
import json

platformUrl = '/service/de/product/platform'
depositInvoiceUrl = '/service/de/deposit/deposit/invoice'
#---------------------------------------------------------------------
depositInvoiceCode = 6814812
#---------------------------------------------------------------------

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
    #@task(100)
    def depositInvoice_get(self):
        self.get(self.addCode(depositInvoiceUrl, depositInvoiceCode))
    @task(100)
    def cifRealCustomer_get(self):
        self.get("/service/platform/parameter-groups")
#--------------------------------------------
    
    #@task(5)
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


class WebsiteUser(HttpLocust):
    # locust.stats.CSV_STATS_INTERVAL_SEC = 5 # default is 2 seconds
    task_set = UserBehavior
    min_wait = 500
    max_wait = 1000
    stop_timeout = 10000
    #host = "http://10.12.47.60:8181"