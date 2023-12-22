# OrderFiscalEntityRequest

Fiscal entity of the order, Currently it is a purely informative field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**FiscalEntityAddress**](FiscalEntityAddress.md) |  | 
**email** | **str** | Email of the fiscal entity | [optional] 
**metadata** | **Dict[str, object]** | Metadata associated with the fiscal entity | [optional] 
**name** | **str** | Name of the fiscal entity | [optional] 
**phone** | **str** | Phone of the fiscal entity | [optional] 
**tax_id** | **str** | Tax ID of the fiscal entity | [optional] 

## Example

```python
from conekta.models.order_fiscal_entity_request import OrderFiscalEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderFiscalEntityRequest from a JSON string
order_fiscal_entity_request_instance = OrderFiscalEntityRequest.from_json(json)
# print the JSON string representation of the object
print OrderFiscalEntityRequest.to_json()

# convert the object into a dict
order_fiscal_entity_request_dict = order_fiscal_entity_request_instance.to_dict()
# create an instance of OrderFiscalEntityRequest from a dict
order_fiscal_entity_request_form_dict = order_fiscal_entity_request.from_dict(order_fiscal_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


