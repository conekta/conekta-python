# EventsResendResponse

event model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_attempts** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**last_attempted_at** | **int** |  | [optional] 
**last_http_response_status** | **int** |  | [optional] 
**response_data** | **Dict[str, object]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from conekta.models.events_resend_response import EventsResendResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventsResendResponse from a JSON string
events_resend_response_instance = EventsResendResponse.from_json(json)
# print the JSON string representation of the object
print(EventsResendResponse.to_json())

# convert the object into a dict
events_resend_response_dict = events_resend_response_instance.to_dict()
# create an instance of EventsResendResponse from a dict
events_resend_response_from_dict = EventsResendResponse.from_dict(events_resend_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


