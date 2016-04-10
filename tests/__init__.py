#!/usr/bin/python
# coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

import unittest
import random
import conekta


class BaseEndpointTestCase(unittest.TestCase):
    random.seed()

    client = conekta

    card_charge_object = {
        "description": "Grad Stogies: Second Class",
        "amount": 20000,
        "currency": "MXN",
        "reference_id": "9893-cohib_s1_wolf_pack",
        "card": "tok_test_visa_4242",
        "details": {
            "name": "Wolverine",
            "email": "logan.thomas@xmen.org",
            "phone": "403-342-0642",
            "line_items": [{
              "name": "Shades",
              "description": "Imported From Mex.",
              "unit_price": 20000,
              "quantity": 1,
              "sku": "cohb_s1",
              "category": "eyewear"
           }]
        }
    }

    cash_charge_object = {
        "currency": "MXN",
        "amount": 20000,
        "description": "Grad Stogies: Second Class",
        "reference_id": "9893-cohib_s1_wolf_pack",
        "cash": {
            "type": "oxxo"
        },
        "details": {
            "name": "Wolverine",
            "email": "logan.thomas@xmen.org",
            "phone": "403-342-0642",
            "line_items": [{
              "name": "Shades",
              "description": "Imported From Mex.",
              "unit_price": 20000,
              "quantity": 1,
              "sku": "cohb_s1",
              "category": "eyewear"
           }]
        }
    }

    bank_charge_object = {
        "currency": "MXN",
        "amount": 20000,
        "description": "Grad Stogies: Second Class",
        "reference_id": "9893-cohib_s1_wolf_pack",
        "bank": {
            "type": "banorte"
        },
        "details": {
            "name": "Wolverine",
            "email": "logan.thomas@xmen.org",
            "phone": "403-342-0642",
            "line_items": [{
              "name": "Shades",
              "description": "Imported From Mex.",
              "unit_price": 20000,
              "quantity": 1,
              "sku": "cohb_s1",
              "category": "eyewear"
           }]
        }
    }

    spei_charge_object = {
        "currency": "MXN",
        "amount": 20000,
        "description": "Grad Stogies: Second Class",
        "reference_id": "9893-cohib_s1_wolf_pack",
        "bank": {
            "type": "spei"
        },
        "details": {
            "name": "Wolverine",
            "email": "logan.thomas@xmen.org",
            "phone": "403-342-0642",
            "line_items": [{
              "name": "Shades",
              "description": "Imported From Mex.",
              "unit_price": 20000,
              "quantity": 1,
              "sku": "cohb_s1",
              "category": "eyewear"
           }]
        }
    }

    plan_object = {
        'id':'py_test_plan_' + str(random.randint(1, 1000000)),
        'name': 'Python Test Subscription',
        'amount': 10000,
        'currency': 'MXN',
        'interval': 'week',
        'frequency': 3
    }

    customer_object = {
        'name':'Logan',
        'email':'logan@x-men.org',
        'phone':'403-342-0642',
        'cards':['tok_test_visa_4242', 'tok_test_mastercard_5100']
    }

    payee_object = {
        'name': 'Graydon Creed',
        'email': 'graydon@friendsofhumanity.com',
        'phone': '5555555555',
        'bank': {
            'account_number': '123456789012345673',
            'account_holder': 'Friends of Humanity'
        }
    }

    payout_method_object = {
        'type': 'bank_transfer_payout_method',
        'account_number': '123456789012345673',
        'account_holder': 'Friends of Humanity'
    }

