# OrderResponseShippingContact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**receiver** | **str** |  | [optional] 
**between_streets** | **str** |  | [optional] 
**address** | [**CustomerShippingContactsResponseAddress**](CustomerShippingContactsResponseAddress.md) |  | [optional] 
**parent_id** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**metadata** | **Dict[str, object]** | Metadata associated with the shipping contact | [optional] 
**deleted** | **bool** |  | [optional] 

## Example

```python
from conekta.models.order_response_shipping_contact import OrderResponseShippingContact

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponseShippingContact from a JSON string
order_response_shipping_contact_instance = OrderResponseShippingContact.from_json(json)
# print the JSON string representation of the object
print OrderResponseShippingContact.to_json()

# convert the object into a dict
order_response_shipping_contact_dict = order_response_shipping_contact_instance.to_dict()
# create an instance of OrderResponseShippingContact from a dict
order_response_shipping_contact_form_dict = order_response_shipping_contact.from_dict(order_response_shipping_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


