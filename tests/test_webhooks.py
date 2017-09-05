#!/usr/bin/python
#coding: utf-8
#(c) 2016- Leo Fischer / Conekta <@leofischer/@conektaio>

from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):
    def test_1_webhooks(self):
        url = 'https://www.example.com'
        url2 = url + '/new_endpoint' 

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        webhook = self.client.Webhook.create({'url':url})
        assert webhook.url == url
        webhook.update({'url':url2})
        assert webhook.url == url2
        webhook.delete()
        assert webhook.deleted
