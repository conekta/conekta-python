# CustomerShippingContactsResponse

Contains the detail of the shipping addresses that the client has active or has used in Conekta

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** |  | [optional] 
**receiver** | **str** |  | [optional] 
**between_streets** | **str** |  | [optional] 
**address** | [**CustomerShippingContactsResponseAddress**](CustomerShippingContactsResponseAddress.md) |  | [optional] 
**parent_id** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**object** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 

## Example

```python
from conekta.models.customer_shipping_contacts_response import CustomerShippingContactsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerShippingContactsResponse from a JSON string
customer_shipping_contacts_response_instance = CustomerShippingContactsResponse.from_json(json)
# print the JSON string representation of the object
print CustomerShippingContactsResponse.to_json()

# convert the object into a dict
customer_shipping_contacts_response_dict = customer_shipping_contacts_response_instance.to_dict()
# create an instance of CustomerShippingContactsResponse from a dict
customer_shipping_contacts_response_form_dict = customer_shipping_contacts_response.from_dict(customer_shipping_contacts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


