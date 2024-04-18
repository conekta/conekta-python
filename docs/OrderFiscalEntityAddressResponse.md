# OrderFiscalEntityAddressResponse

Address of the fiscal entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street1** | **str** | Street name and number | 
**street2** | **str** | Street name and number | [optional] 
**postal_code** | **str** | Postal code | 
**city** | **str** | City | 
**state** | **str** | State | [optional] 
**country** | **str** | this field follows the [ISO 3166-1 alpha-2 standard](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) | 
**external_number** | **str** | External number | 
**object** | **str** |  | [optional] 

## Example

```python
from conekta.models.order_fiscal_entity_address_response import OrderFiscalEntityAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderFiscalEntityAddressResponse from a JSON string
order_fiscal_entity_address_response_instance = OrderFiscalEntityAddressResponse.from_json(json)
# print the JSON string representation of the object
print(OrderFiscalEntityAddressResponse.to_json())

# convert the object into a dict
order_fiscal_entity_address_response_dict = order_fiscal_entity_address_response_instance.to_dict()
# create an instance of OrderFiscalEntityAddressResponse from a dict
order_fiscal_entity_address_response_from_dict = OrderFiscalEntityAddressResponse.from_dict(order_fiscal_entity_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


