# UpdateOrderTaxResponse

create new taxes for an existing order response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount to be collected for tax in cents | 
**description** | **str** | description or tax&#39;s name | 
**metadata** | **Dict[str, object]** |  | [optional] 
**id** | **str** |  | 
**object** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 

## Example

```python
from conekta.models.update_order_tax_response import UpdateOrderTaxResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderTaxResponse from a JSON string
update_order_tax_response_instance = UpdateOrderTaxResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderTaxResponse.to_json())

# convert the object into a dict
update_order_tax_response_dict = update_order_tax_response_instance.to_dict()
# create an instance of UpdateOrderTaxResponse from a dict
update_order_tax_response_from_dict = UpdateOrderTaxResponse.from_dict(update_order_tax_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


