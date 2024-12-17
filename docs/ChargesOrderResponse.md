# ChargesOrderResponse

The charges associated with the order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**data** | [**List[ChargesOrderResponseAllOfData]**](ChargesOrderResponseAllOfData.md) |  | [optional] 

## Example

```python
from conekta.models.charges_order_response import ChargesOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargesOrderResponse from a JSON string
charges_order_response_instance = ChargesOrderResponse.from_json(json)
# print the JSON string representation of the object
print(ChargesOrderResponse.to_json())

# convert the object into a dict
charges_order_response_dict = charges_order_response_instance.to_dict()
# create an instance of ChargesOrderResponse from a dict
charges_order_response_from_dict = ChargesOrderResponse.from_dict(charges_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


