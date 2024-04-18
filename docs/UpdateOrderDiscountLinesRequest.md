# UpdateOrderDiscountLinesRequest

List of discounts that apply to the order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**code** | **str** | Discount code. | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from conekta.models.update_order_discount_lines_request import UpdateOrderDiscountLinesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderDiscountLinesRequest from a JSON string
update_order_discount_lines_request_instance = UpdateOrderDiscountLinesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderDiscountLinesRequest.to_json())

# convert the object into a dict
update_order_discount_lines_request_dict = update_order_discount_lines_request_instance.to_dict()
# create an instance of UpdateOrderDiscountLinesRequest from a dict
update_order_discount_lines_request_from_dict = UpdateOrderDiscountLinesRequest.from_dict(update_order_discount_lines_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


