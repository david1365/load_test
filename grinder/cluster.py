#!/usr/bin/env python
# -*- coding: utf-8 -*-

from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest
from HTTPClient import NVPair
import simplejson as json

from datetime import timedelta
from datetime import datetime

host = "http://10.12.47.125"

loginUrl = '/service/platform/authentication/login'
refreshTokenUrl = '/service/platform/authentication/refresh'

depositInvoiceUrl = '/service/platform/menuHierarchyService'

depositInvoiceCode = 6814812

testNumber = 0

headers = [
    NVPair('Content-Type', 'application/json'),
    NVPair('Charset', 'UTF-8'),
]

refreshTokenInterval = 1  # minuts


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


def createRequestWithoutTest():
    global testNumber
    global headers
    request = HTTPRequest(url=host)
    request.headers = headers
    return request


# ----get------------------------------------------------------------
depositInvoiceRequest_get = createRequest("deposit Invoice request(GET)")

# ----TokenRequest------------------------------------------------------------
loginRequest_post = createRequestWithoutTest()
refreshTokenRequest_get = createRequestWithoutTest()


class TestRunner:
    token = None

    headers = None

    totalTestCount = 2

    testCounter = 1

    refreshTime = None

    def refreshTokenDecider(self):
        now = datetime.now()
        if now >= self.refreshTime:
            self.refreshToken_get(now)

    # -----------------------------------------------------------------
    def addCode(self, url, code):
        return url + '/' + str(code)

    # ---get------------------------------------------------------------------------------------------

    def depositInvoice_get(self):
        depositInvoiceRequest_get.GET(depositInvoiceUrl, None, self.headers)

    # ----Token---------------------------------------------------------------------------------------------
    def refreshToken_get(self, now):
        self.refreshTime = calculateRefreshTokenTime(now)
        response = refreshTokenRequest_get.GET(refreshTokenUrl, None, self.headers)
        self.token = pickUpToken(response)

    def login_post(self, payload):
        return loginRequest_post.POST(loginUrl, json.dumps(payload))

    def __init__(self):
        payload = {
            "username": "test456",
            "password": "1234"
        }

        self.refreshTime = calculateRefreshTokenTime(datetime.now())

        response = self.login_post(payload)
        self.token = pickUpToken(response)

    def __call__(self):
        self.headers = [
            NVPair('Content-Type', 'application/json'),
            NVPair('Charset', 'UTF-8'),
            NVPair('Authorization', self.token)
        ]

        if self.testCounter == 1:
            self.depositInvoice_get()
        elif self.testCounter == 2:
            self.refreshTokenDecider()

        if self.testCounter >= self.totalTestCount:
            self.testCounter = 1
        else:
            self.testCounter += 1
