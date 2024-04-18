# OrderResponseDiscountLines


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**data** | [**List[DiscountLinesDataResponse]**](DiscountLinesDataResponse.md) |  | [optional] 

## Example

```python
from conekta.models.order_response_discount_lines import OrderResponseDiscountLines

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponseDiscountLines from a JSON string
order_response_discount_lines_instance = OrderResponseDiscountLines.from_json(json)
# print the JSON string representation of the object
print(OrderResponseDiscountLines.to_json())

# convert the object into a dict
order_response_discount_lines_dict = order_response_discount_lines_instance.to_dict()
# create an instance of OrderResponseDiscountLines from a dict
order_response_discount_lines_from_dict = OrderResponseDiscountLines.from_dict(order_response_discount_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


