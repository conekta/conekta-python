# OrderChargesResponse

The charges associated with the order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**data** | [**List[ChargesDataResponse]**](ChargesDataResponse.md) |  | [optional] 

## Example

```python
from conekta.models.order_charges_response import OrderChargesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChargesResponse from a JSON string
order_charges_response_instance = OrderChargesResponse.from_json(json)
# print the JSON string representation of the object
print(OrderChargesResponse.to_json())

# convert the object into a dict
order_charges_response_dict = order_charges_response_instance.to_dict()
# create an instance of OrderChargesResponse from a dict
order_charges_response_from_dict = OrderChargesResponse.from_dict(order_charges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


