# CustomerShippingContactsResponseAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**street1** | **str** |  | [optional] 
**street2** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**residential** | **bool** |  | [optional] 

## Example

```python
from conekta.models.customer_shipping_contacts_response_address import CustomerShippingContactsResponseAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerShippingContactsResponseAddress from a JSON string
customer_shipping_contacts_response_address_instance = CustomerShippingContactsResponseAddress.from_json(json)
# print the JSON string representation of the object
print(CustomerShippingContactsResponseAddress.to_json())

# convert the object into a dict
customer_shipping_contacts_response_address_dict = customer_shipping_contacts_response_address_instance.to_dict()
# create an instance of CustomerShippingContactsResponseAddress from a dict
customer_shipping_contacts_response_address_from_dict = CustomerShippingContactsResponseAddress.from_dict(customer_shipping_contacts_response_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


