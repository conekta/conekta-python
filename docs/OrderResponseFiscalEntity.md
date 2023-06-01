# OrderResponseFiscalEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**OrderResponseFiscalEntityAddress**](OrderResponseFiscalEntityAddress.md) |  | [optional] 
**tax_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 

## Example

```python
from conekta.models.order_response_fiscal_entity import OrderResponseFiscalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponseFiscalEntity from a JSON string
order_response_fiscal_entity_instance = OrderResponseFiscalEntity.from_json(json)
# print the JSON string representation of the object
print OrderResponseFiscalEntity.to_json()

# convert the object into a dict
order_response_fiscal_entity_dict = order_response_fiscal_entity_instance.to_dict()
# create an instance of OrderResponseFiscalEntity from a dict
order_response_fiscal_entity_form_dict = order_response_fiscal_entity.from_dict(order_response_fiscal_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


