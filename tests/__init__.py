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
        'name':'James Howlett',
        'email':'logan@x-men.org',
        'phone':'+525511223344',
        'payment_sources':[
          { 'token_id': 'tok_test_visa_4242',
            'type': 'card'},
          { 'token_id': 'tok_test_mastercard_5100',
            'type': 'card'}
        ],
    "shipping_contacts": [{
        "phone": "+525511223344",
        "receiver": "Marvin Fuller",
        "between_streets": "Ackerman Crescent",
        "address": {
            "street1": "250 Alexis St",
            "city": "Red Deer",
            "state": "Alberta",
            "country": "CA",
            "postal_code": "T4N 0B8"
        }

    }]
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

    order_object = {
      "line_items": [
          {
              "name": "Box of Cohiba S1s",
              "description": "Imported From Mex.",
              "unit_price": 20000,
              "quantity": 1,
              "sku": "cohb_s1",
              "category": "food",
              "type" : "physical",
              "tags" : ["food", "mexican food"]
          }
      ],
      "tax_lines":[
        {
          "description": "IVA",
          "amount": 600,
          "metadata": {
            "random_key": "random_value"
          }
        }],
      "shipping_lines":[
        {
          "amount": 0,
          "tracking_number": "TRACK123",
          "carrier": "USPS",
          "method": "Train",
          "metadata": {
             "random_key": "random_value"
          }
        }],
      "discount_lines":[
        {
          "code": "descuento",
          "type": "loyalty",
          "amount": 600
        }],
      "customer_info":{
          "name": "John Constantine",
          "phone": "+525533445566",
          "email": "john@meh.com",
          "corporate": False,
          "vertical_info": {}
        },
      "shipping_contact":{
          "phone" : "5544332211",
          "receiver": "Marvin Fuller",
          "between_streets": "Ackerman Crescent",
          "address": {
              "street1": "250 Alexis St",
              "state": "Alberta",
              "country": "MX",
              "postal_code": "23455",
              "metadata":{ "soft_validations": True}
          }
      },
      "charges": [{
        "payment_method":{
          "type":"oxxo_cash"
        },
        "amount": 20000
      }],
      "currency" : "mxn",
      "metadata" : {"test" : "extra info"}
    }
    line_item_object = {
        "name": "test line item",
        "description": "Imported From Mex.",
        "unit_price": 10000,
        "quantity": 2,
        "sku": "noSKU",
        "category": "food",
        "type" : "physical",
        "tags" : ["food", "mexican food"]
    }
    tax_line_object = {
        "description": "IVA2",
        "amount": 600,
        "metadata": {
        "random_key": "random_value"
        }
    }

    shipping_lines_object = {
        "amount": 0,
        "tracking_number": "TRACK123",
        "carrier": "USPS",
        "method": "Train",
        "metadata": {
           "random_key": "random_value"
        }
    }

    discount_line_object = {
        "code": "descuento",
        "type": "loyalty",
        "amount": 100
    }

    order_shipping_contact_object = {
      "shipping_contact": {
        "phone" : "+525511223399",
        "receiver": "Marvin Fuller",
        "between_streets": "Ackerman Crescent",
        "address": {
            "street1": "250 Alexis St",
            "state": "Alberta",
            "country": "MX",
            "postal_code": "23455",
            "metadata":{ "soft_validations": True}
          }
      }
    }

    charge_object = {
      "payment_method":{
        "type":"oxxo_cash"
      },
      "amount": 20000
    }

    payment_source_object = {
      'token_id': 'tok_test_visa_4242',
      'type': 'card'
    }

    update_payment_source_object = {
        "name": "Emiliano Cabrera",
        "exp_month": "12",
        "exp_year": "20",
        "address": {
            "street1": "Nuevo leon",
            "city": "Monterrey",
            "state": "Nuevo Leon",
            "country": "MX",
            "postal_code": "64700"
        }
    }

    shipping_contact_object = {
        "phone": "+525511008811",
        "receiver": "Dr. Manhatan",
        "between_streets": "some streets",
        "address": {
            "street1": "250 Alexis St",
            "city": "Red Deer",
            "state": "Alberta",
            "country": "CA",
            "postal_code": "T4N 0B8"
        }
    }

    checkout_object = {
        "name": "Payment Link Name",
        "type": "PaymentLink",
        "recurrent": False,
        "expired_at": 1590882634,
        "allowed_payment_methods": ["cash", "card", "bank_transfer"],
        "needs_shipping_contact": True,
        "monthly_installments_enabled": False,
        "monthly_installments_options": [3, 6, 9, 12],
        "order_template": {
            "line_items": [{
                "name": "Red Wine",
                "unit_price": 1000,
                "quantity": 10
            }],
        "currency": "MXN",
        "customer_info": {
              "name": "Juan Perez",
              "email": "test@conekta.com",
              "phone": "5566982090"
        }
      }
    }

    checkout_object_multiple = {
        "name": "Payment Link Name",
        "type": "PaymentLink",
        "recurrent": True,
        "expired_at": 1590882634,
        "allowed_payment_methods": ["cash", "card", "bank_transfer"],
        "needs_shipping_contact": True,
        "monthly_installments_enabled": False,
        "monthly_installments_options": [3, 6, 9, 12],
        "order_template": {
            "line_items": [{
                "name": "Red Wine",
                "unit_price": 1000,
                "quantity": 10
            }],
        "currency": "MXN",
        "customer_info": {
              "name": "Juan Perez",
              "email": "test@conekta.com",
              "phone": "5566982090"
        }
      }
    }

    checkout_object_msi = {
        "name": "Payment Link Name",
        "type": "PaymentLink",
        "recurrent": True,
        "expired_at": 1590882634,
        "allowed_payment_methods": ["cash", "card", "bank_transfer"],
        "needs_shipping_contact": True,
        "monthly_installments_enabled": True,
        "monthly_installments_options": [3, 6, 9, 12],
        "order_template": {
            "line_items": [{
                "name": "Red Wine",
                "unit_price": 1000,
                "quantity": 10
            }],
        "currency": "MXN",
        "customer_info": {
              "name": "Juan Perez",
              "email": "test@conekta.com",
              "phone": "5566982090"
        }
      }
    }

    checkout_object_type_checkout = {
        "name": "Payment Link Name",
        "type": "checkout",
        "recurrent": True,
        "expired_at": 1590882634,
        "allowed_payment_methods": ["cash", "card", "bank_transfer"],
        "needs_shipping_contact": True,
        "monthly_installments_enabled": True,
        "monthly_installments_options": [3, 6, 9, 12],
        "order_template": {
            "line_items": [{
                "name": "Red Wine",
                "unit_price": 1000,
                "quantity": 10
            }],
        "currency": "MXN",
        "customer_info": {
              "name": "Juan Perez",
              "email": "test@conekta.com",
              "phone": "5566982090"
        }
      }
    }

        checkout_object_send = {
        "id": "05b25724-df59-4925-8762-105d627875fd"
        "name": "Payment Link Name",
        "type": "checkout",
        "recurrent": True,
        "expired_at": 1590882634,
        "allowed_payment_methods": ["cash", "card", "bank_transfer"],
        "needs_shipping_contact": True,
        "monthly_installments_enabled": True,
        "monthly_installments_options": [3, 6, 9, 12],
        "order_template": {
            "line_items": [{
                "name": "Red Wine",
                "unit_price": 1000,
                "quantity": 10
            }],
        "currency": "MXN",
        "customer_info": {
              "name": "Juan Perez",
              "email": "test@conekta.com",
              "phone": "5566982090"
        }
      }
    }


    checkout_order_object = 
        "currency": "MXN",
        "customer_info": {
           "customer_id": "cus_2o3FvMEBiKitVK1vQ"
        },
       "line_items": [{
           "name": "Box of Cohiba S1s",
           "unit_price": 300000,
           "quantity": 1
       }],
       "shipping_lines": [{
           "amount": 0
       }],
       "checkout": {
           "allowed_payment_methods": ["cash", "card", "bank_transfer"],
           "multifactor_authentication": False,
           "monthly_installments_enabled": False,
           "monthly_installments_options": [3,6,9,12,18],
           "expires_at": 1609891200
        },
       "shipping_contact": {
          "phone": "+5215555555555",
          "receiver": "Marvin Fuller",
          "address": {
            "street1": "Nuevo Leon 4",
            "country": "MX",
            "postal_code": "06100"
          }
       }

    checkout_msi_order__object = 
        "currency": "MXN",
        "customer_info": {
           "customer_id": "cus_2o3FvMEBiKitVK1vQ"
        },
       "line_items": [{
           "name": "Box of Cohiba S1s",
           "unit_price": 300000,
           "quantity": 1
       }],
       "shipping_lines": [{
           "amount": 0
       }],
       "checkout": {
           "type":"Integration",
           "allowed_payment_methods": ["cash", "card", "bank_transfer"],
           "multifactor_authentication": False,
           "monthly_installments_enabled": True,
           "monthly_installments_options": [3,6,9,12,18],
           "expires_at": 1609891200
        },
       "shipping_contact": {
          "phone": "+5215555555555",
          "receiver": "Marvin Fuller",
          "address": {
            "street1": "Nuevo Leon 4",
            "country": "MX",
            "postal_code": "06100"
          }
       }


          checkout_order__redirect_object = 
        "currency": "MXN",
        "customer_info": {
           "customer_id": "cus_2o3FvMEBiKitVK1vQ"
        },
       "line_items": [{
           "name": "Box of Cohiba S1s",
           "unit_price": 300000,
           "quantity": 1
       }],
       "shipping_lines": [{
           "amount": 0
       }],
       "checkout": {
           "type":"HostedPayment",
           "success_url": "testredirect.com",
           "failure_url": "testredirect.com",
           "allowed_payment_methods": ["cash", "card", "bank_transfer"],
           "multifactor_authentication": False,
           "monthly_installments_enabled": False,
           "monthly_installments_options": [3,6,9,12,18],
           "expires_at": 1609891200
        },
       "shipping_contact": {
          "phone": "+5215555555555",
          "receiver": "Marvin Fuller",
          "address": {
            "street1": "Nuevo Leon 4",
            "country": "MX",
            "postal_code": "06100"
          }
       }