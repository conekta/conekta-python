# OrderChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment** | **str** |  | [optional] 
**checkout_request_id** | **str** |  | [optional] 
**checkout_request_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from conekta.models.order_channel_response import OrderChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelResponse from a JSON string
order_channel_response_instance = OrderChannelResponse.from_json(json)
# print the JSON string representation of the object
print(OrderChannelResponse.to_json())

# convert the object into a dict
order_channel_response_dict = order_channel_response_instance.to_dict()
# create an instance of OrderChannelResponse from a dict
order_channel_response_from_dict = OrderChannelResponse.from_dict(order_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


