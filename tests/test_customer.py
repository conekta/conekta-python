#!/usr/bin/python
#coding: utf-8
#(c) 2017 Ramses Carbajal <@RamsesCarbajal>
from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_01_customer_create(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.create(self.customer_object.copy())
        payment_source = customer.payment_sources[0]
        fiscal_entity = customer.fiscal_entities[0]
        shipping_contact = customer.shipping_contacts[0]
        
        assert customer.name  == 'James Howlett'
        assert customer.email == 'logan@x-men.org'
        assert customer.phone == '+525511223344'

        assert payment_source.brand == 'VISA'
        assert payment_source.last4 == '4242'
        assert payment_source.type  == 'card'

        assert fiscal_entity.tax_id          == 'AMGH851205MN1'
        assert fiscal_entity.name            == 'Nike SA de CV'
        assert fiscal_entity.address.street1 == '250 Alexis St'

        assert shipping_contact.receiver        == "Marvin Fuller"
        assert shipping_contact.between_streets == "Ackerman Crescent"
        assert shipping_contact.address.city    == "Red Deer"

    
    def test_02_customer_add_token(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer_params = self.customer_object.copy()
        del customer_params["payment_sources"]
        customer = self.client.Customer.create(customer_params)
        payment_source = customer.createPaymentSource(self.payment_source_object.copy())

        assert payment_source.brand == "VISA"
        assert payment_source.last4 == "4242"

    def test_03_customer_update_payment_source(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.create(self.customer_object.copy())
        payment_source = customer.payment_sources[0]
        payment_source.update(self.update_payment_source_object.copy())
        payment_source = customer.payment_sources[0]    
        assert payment_source.brand == "VISA"
        assert payment_source.last4 == "4242"

    def test_04_customer_delete_payment_source(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.create(self.customer_object.copy())
        payment_source = customer.payment_sources[0]

        payment_source_deleted = payment_source.delete()

        assert payment_source_deleted.deleted == True

        payment_source = customer.payment_sources[0]

        assert payment_source.last4 == "5100"
        assert payment_source.brand == "MC"

    def test_05_customer_add_fiscal_entity(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer_params = self.customer_object.copy()
        del customer_params["fiscal_entities"]
        customer = self.client.Customer.create(customer_params)
        fiscal_entity = customer.createFiscalEntity(self.fiscal_entities_object.copy())

        assert fiscal_entity.tax_id == "DKLS8205219WD"
        assert fiscal_entity.name   == "MEH S.A. DE C.V."
    
    def test_06_customer_update_fiscal_entity(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer_params = self.customer_object.copy()
        customer = self.client.Customer.create(customer_params)
        fiscal_entity = customer.fiscal_entities[0]

        fiscal_entity.update(self.fiscal_entities_object.copy())

        fiscal_entity = customer.fiscal_entities[0]        
        assert fiscal_entity.tax_id == "DKLS8205219WD"

    def test_07_customer_delete_fiscal_entity(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.create(self.customer_object.copy())
        customer.createFiscalEntity(self.fiscal_entities_object.copy())
        fiscal_entity = customer.fiscal_entities[0]

        fiscal_entity_deleted = fiscal_entity.delete()

        assert fiscal_entity_deleted.deleted == True

        fiscal_entity = customer.fiscal_entities[0]

      
        assert fiscal_entity.tax_id == "DKLS8205219WD"
        assert fiscal_entity.name   == "MEH S.A. DE C.V."

    def test_08_customer_add_shipping_contact(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer_params = self.customer_object.copy()
        del customer_params["shipping_contacts"]
        customer = self.client.Customer.create(customer_params)
        shipping_contact = customer.createShippingContact(self.shipping_contact_object.copy())

        assert shipping_contact.phone           == "+525511008811"
        assert shipping_contact.receiver        == "Dr. Manhatan"
        assert shipping_contact.between_streets == "some streets"
    
    def test_06_customer_update_fiscal_entity(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer_params = self.customer_object.copy()
        customer = self.client.Customer.create(customer_params)
        shipping_contact = customer.shipping_contacts[0]

        shipping_contact.update(self.shipping_contact_object.copy())

        assert shipping_contact.phone           == "+525511008811"
        assert shipping_contact.receiver        == "Dr. Manhatan"
        assert shipping_contact.between_streets == "some streets"

    def test_07_customer_delete_fiscal_entity(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.create(self.customer_object.copy())
        customer.createShippingContact(self.shipping_contact_object.copy())
        shipping_contact = customer.shipping_contacts[0]

        shipping_contact_deleted = shipping_contact.delete()

        assert shipping_contact_deleted.deleted == True

        shipping_contact = customer.shipping_contacts[0]

        assert shipping_contact.phone           == "+525511008811"
        assert shipping_contact.receiver        == "Dr. Manhatan"
        assert shipping_contact.between_streets == "some streets"
