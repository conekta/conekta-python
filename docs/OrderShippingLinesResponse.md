# OrderShippingLinesResponse

List of shipping costs applied to the order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[ShippingLinesDataResponse]**](ShippingLinesDataResponse.md) |  | [optional] 

## Example

```python
from conekta.models.order_shipping_lines_response import OrderShippingLinesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderShippingLinesResponse from a JSON string
order_shipping_lines_response_instance = OrderShippingLinesResponse.from_json(json)
# print the JSON string representation of the object
print(OrderShippingLinesResponse.to_json())

# convert the object into a dict
order_shipping_lines_response_dict = order_shipping_lines_response_instance.to_dict()
# create an instance of OrderShippingLinesResponse from a dict
order_shipping_lines_response_from_dict = OrderShippingLinesResponse.from_dict(order_shipping_lines_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


