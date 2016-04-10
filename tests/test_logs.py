#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>
#(c) 2014- Leo Fischer / Conekta <@leofischer/@conektaio>

from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_01_log_complete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        logs = self.client.Log.where({})
        self.assertIsInstance(logs[0], self.client.Log)
        retrieved_log = self.client.Log.find(logs[0].id)
        assert retrieved_log.id
