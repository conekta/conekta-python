# CustomerShippingContactsAddress

Address of the person who will receive the order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street1** | **str** |  | [optional] 
**street2** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** | this field follows the [ISO 3166-1 alpha-2 standard](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) | [optional] 
**residential** | **bool** |  | [optional] 

## Example

```python
from conekta.models.customer_shipping_contacts_address import CustomerShippingContactsAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerShippingContactsAddress from a JSON string
customer_shipping_contacts_address_instance = CustomerShippingContactsAddress.from_json(json)
# print the JSON string representation of the object
print CustomerShippingContactsAddress.to_json()

# convert the object into a dict
customer_shipping_contacts_address_dict = customer_shipping_contacts_address_instance.to_dict()
# create an instance of CustomerShippingContactsAddress from a dict
customer_shipping_contacts_address_form_dict = customer_shipping_contacts_address.from_dict(customer_shipping_contacts_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


