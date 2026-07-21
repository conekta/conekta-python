# OrderTaxResponse

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
from conekta.models.order_tax_response import OrderTaxResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderTaxResponse from a JSON string
order_tax_response_instance = OrderTaxResponse.from_json(json)
# print the JSON string representation of the object
print(OrderTaxResponse.to_json())

# convert the object into a dict
order_tax_response_dict = order_tax_response_instance.to_dict()
# create an instance of OrderTaxResponse from a dict
order_tax_response_from_dict = OrderTaxResponse.from_dict(order_tax_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


