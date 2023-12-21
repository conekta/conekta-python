# OrderFiscalEntityResponse

Fiscal entity of the order, Currently it is a purely informative field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**OrderFiscalEntityAddressResponse**](OrderFiscalEntityAddressResponse.md) |  | 
**email** | **str** | Email of the fiscal entity | [optional] 
**metadata** | **Dict[str, object]** | Metadata associated with the fiscal entity | [optional] 
**name** | **str** | Name of the fiscal entity | [optional] 
**tax_id** | **str** | Tax ID of the fiscal entity | [optional] 
**id** | **str** | ID of the fiscal entity | 
**created_at** | **int** | The time at which the object was created in seconds since the Unix epoch | 
**object** | **str** |  | 
**phone** | **str** | Phone of the fiscal entity | [optional] 

## Example

```python
from conekta.models.order_fiscal_entity_response import OrderFiscalEntityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderFiscalEntityResponse from a JSON string
order_fiscal_entity_response_instance = OrderFiscalEntityResponse.from_json(json)
# print the JSON string representation of the object
print OrderFiscalEntityResponse.to_json()

# convert the object into a dict
order_fiscal_entity_response_dict = order_fiscal_entity_response_instance.to_dict()
# create an instance of OrderFiscalEntityResponse from a dict
order_fiscal_entity_response_form_dict = order_fiscal_entity_response.from_dict(order_fiscal_entity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


