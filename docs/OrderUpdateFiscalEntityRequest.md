# OrderUpdateFiscalEntityRequest

Fiscal entity of the order, Currently it is a purely informative field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**FiscalEntityAddress**](FiscalEntityAddress.md) |  | 
**email** | **str** | Email of the fiscal entity | [optional] 
**name** | **str** | Name of the fiscal entity | [optional] 
**metadata** | **Dict[str, object]** | Metadata associated with the fiscal entity | [optional] 
**phone** | **str** | Phone of the fiscal entity | [optional] 
**tax_id** | **str** | Tax ID of the fiscal entity | [optional] 

## Example

```python
from conekta.models.order_update_fiscal_entity_request import OrderUpdateFiscalEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderUpdateFiscalEntityRequest from a JSON string
order_update_fiscal_entity_request_instance = OrderUpdateFiscalEntityRequest.from_json(json)
# print the JSON string representation of the object
print(OrderUpdateFiscalEntityRequest.to_json())

# convert the object into a dict
order_update_fiscal_entity_request_dict = order_update_fiscal_entity_request_instance.to_dict()
# create an instance of OrderUpdateFiscalEntityRequest from a dict
order_update_fiscal_entity_request_from_dict = OrderUpdateFiscalEntityRequest.from_dict(order_update_fiscal_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


