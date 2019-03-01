# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class VerificationTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v1.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .verifications.create(to="to", channel="channel")

        values = {'To': "to", 'Channel': "channel", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v1/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Verifications',
            data=values,
        ))

    def test_create_verification_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+14159373912",
                "channel": "sms",
                "status": "pending",
                "valid": null,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {
                    "carrier": {
                        "error_code": null,
                        "name": "Carrier Name",
                        "mobile_country_code": "310",
                        "mobile_network_code": "150",
                        "type": "mobile"
                    }
                },
                "amount": "$29.99",
                "payee": "Acme",
                "url": "https://verify.twilio.com/v1/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v1.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications.create(to="to", channel="channel")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v1.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .verifications(sid="sid").update(status="canceled")

        values = {'Status': "canceled", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v1/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Verifications/sid',
            data=values,
        ))

    def test_update_verification_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+14159373912",
                "channel": "sms",
                "status": "canceled",
                "valid": null,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {
                    "carrier": {
                        "error_code": null,
                        "name": "Carrier Name",
                        "mobile_country_code": "310",
                        "mobile_network_code": "150",
                        "type": "mobile"
                    }
                },
                "amount": "$29.99",
                "payee": "Acme",
                "url": "https://verify.twilio.com/v1/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v1.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications(sid="sid").update(status="canceled")

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v1.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .verifications(sid="sid").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v1/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Verifications/sid',
        ))

    def test_fetch_verification_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+14159373912",
                "channel": "sms",
                "status": "pending",
                "valid": null,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {
                    "carrier": {
                        "error_code": null,
                        "name": "Carrier Name",
                        "mobile_country_code": "310",
                        "mobile_network_code": "150",
                        "type": "mobile"
                    }
                },
                "amount": "$29.99",
                "payee": "Acme",
                "url": "https://verify.twilio.com/v1/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v1.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications(sid="sid").fetch()

        self.assertIsNotNone(actual)
