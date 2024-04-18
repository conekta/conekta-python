# OrderTaxRequest

create new taxes for an existing order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount to be collected for tax in cents | 
**description** | **str** | description or tax&#39;s name | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from conekta.models.order_tax_request import OrderTaxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderTaxRequest from a JSON string
order_tax_request_instance = OrderTaxRequest.from_json(json)
# print the JSON string representation of the object
print(OrderTaxRequest.to_json())

# convert the object into a dict
order_tax_request_dict = order_tax_request_instance.to_dict()
# create an instance of OrderTaxRequest from a dict
order_tax_request_from_dict = OrderTaxRequest.from_dict(order_tax_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


