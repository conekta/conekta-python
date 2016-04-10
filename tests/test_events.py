#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>
#(c) 2014- Leo Fischer / Conekta <@leofischer/@conektaio>

from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_01_event_complete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        events = self.client.Event.where({})
        self.assertIsInstance(events[0], self.client.Event)
        retrieved_event = self.client.Event.find(events[0].id)
        assert retrieved_event.id
