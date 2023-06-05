# OrderRefundRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 
**expires_at** | **int** |  | [optional] 
**reason** | **str** |  | 

## Example

```python
from conekta.models.order_refund_request import OrderRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRefundRequest from a JSON string
order_refund_request_instance = OrderRefundRequest.from_json(json)
# print the JSON string representation of the object
print OrderRefundRequest.to_json()

# convert the object into a dict
order_refund_request_dict = order_refund_request_instance.to_dict()
# create an instance of OrderRefundRequest from a dict
order_refund_request_form_dict = order_refund_request.from_dict(order_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


