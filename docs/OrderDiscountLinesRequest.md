# OrderDiscountLinesRequest

List of discounts that apply to the order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount to be deducted from the total sum of all payments, in cents. | 
**code** | **str** | Discount code. | 
**type** | **str** | It can be &#39;loyalty&#39;, &#39;campaign&#39;, &#39;coupon&#39; o &#39;sign&#39; | 

## Example

```python
from conekta.models.order_discount_lines_request import OrderDiscountLinesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDiscountLinesRequest from a JSON string
order_discount_lines_request_instance = OrderDiscountLinesRequest.from_json(json)
# print the JSON string representation of the object
print(OrderDiscountLinesRequest.to_json())

# convert the object into a dict
order_discount_lines_request_dict = order_discount_lines_request_instance.to_dict()
# create an instance of OrderDiscountLinesRequest from a dict
order_discount_lines_request_from_dict = OrderDiscountLinesRequest.from_dict(order_discount_lines_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


