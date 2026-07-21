# OrdersUpdateTaxesRequest

create new taxes for an existing order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount to be collected for tax in cents | [optional] 
**description** | **str** | description or tax&#39;s name | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from conekta.models.orders_update_taxes_request import OrdersUpdateTaxesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersUpdateTaxesRequest from a JSON string
orders_update_taxes_request_instance = OrdersUpdateTaxesRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersUpdateTaxesRequest.to_json())

# convert the object into a dict
orders_update_taxes_request_dict = orders_update_taxes_request_instance.to_dict()
# create an instance of OrdersUpdateTaxesRequest from a dict
orders_update_taxes_request_from_dict = OrdersUpdateTaxesRequest.from_dict(orders_update_taxes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


