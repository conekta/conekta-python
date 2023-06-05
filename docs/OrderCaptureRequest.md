# OrderCaptureRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Amount to capture | 

## Example

```python
from conekta.models.order_capture_request import OrderCaptureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCaptureRequest from a JSON string
order_capture_request_instance = OrderCaptureRequest.from_json(json)
# print the JSON string representation of the object
print OrderCaptureRequest.to_json()

# convert the object into a dict
order_capture_request_dict = order_capture_request_instance.to_dict()
# create an instance of OrderCaptureRequest from a dict
order_capture_request_form_dict = order_capture_request.from_dict(order_capture_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


