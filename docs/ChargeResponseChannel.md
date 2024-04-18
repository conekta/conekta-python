# ChargeResponseChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment** | **str** |  | [optional] 
**checkout_request_id** | **str** |  | [optional] 
**checkout_request_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from conekta.models.charge_response_channel import ChargeResponseChannel

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeResponseChannel from a JSON string
charge_response_channel_instance = ChargeResponseChannel.from_json(json)
# print the JSON string representation of the object
print(ChargeResponseChannel.to_json())

# convert the object into a dict
charge_response_channel_dict = charge_response_channel_instance.to_dict()
# create an instance of ChargeResponseChannel from a dict
charge_response_channel_from_dict = ChargeResponseChannel.from_dict(charge_response_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


