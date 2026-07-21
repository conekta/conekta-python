# CustomerShippingContactsRequest

[Shipping](https://developers.conekta.com/v2.3.0/reference/createcustomershippingcontacts) details, required in case of sending a shipping. If we do not receive a shipping_contact on the order, the default shipping_contact of the customer will be used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Phone contact | [optional] 
**receiver** | **str** | Name of the person who will receive the order | [optional] 
**between_streets** | **str** | The street names between which the order will be delivered. | [optional] 
**address** | [**CustomerShippingContactsRequestAddress**](CustomerShippingContactsRequestAddress.md) |  | 
**parent_id** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**metadata** | **Dict[str, object]** | Metadata associated with the shipping contact | [optional] 

## Example

```python
from conekta.models.customer_shipping_contacts_request import CustomerShippingContactsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerShippingContactsRequest from a JSON string
customer_shipping_contacts_request_instance = CustomerShippingContactsRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerShippingContactsRequest.to_json())

# convert the object into a dict
customer_shipping_contacts_request_dict = customer_shipping_contacts_request_instance.to_dict()
# create an instance of CustomerShippingContactsRequest from a dict
customer_shipping_contacts_request_from_dict = CustomerShippingContactsRequest.from_dict(customer_shipping_contacts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


