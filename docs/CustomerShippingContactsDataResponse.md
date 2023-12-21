# CustomerShippingContactsDataResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Phone contact | [optional] 
**receiver** | **str** | Name of the person who will receive the order | [optional] 
**between_streets** | **str** | The street names between which the order will be delivered. | [optional] 
**address** | [**CustomerShippingContactsAddress**](CustomerShippingContactsAddress.md) |  | 
**parent_id** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**metadata** | **Dict[str, object]** | Metadata associated with the shipping contact | [optional] 
**id** | **str** |  | 
**object** | **str** |  | 
**created_at** | **int** |  | 

## Example

```python
from conekta.models.customer_shipping_contacts_data_response import CustomerShippingContactsDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerShippingContactsDataResponse from a JSON string
customer_shipping_contacts_data_response_instance = CustomerShippingContactsDataResponse.from_json(json)
# print the JSON string representation of the object
print CustomerShippingContactsDataResponse.to_json()

# convert the object into a dict
customer_shipping_contacts_data_response_dict = customer_shipping_contacts_data_response_instance.to_dict()
# create an instance of CustomerShippingContactsDataResponse from a dict
customer_shipping_contacts_data_response_form_dict = customer_shipping_contacts_data_response.from_dict(customer_shipping_contacts_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


