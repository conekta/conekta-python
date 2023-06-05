# EventResponse

event model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**id** | **str** |  | [optional] 
**livemode** | **bool** |  | [optional] 
**object** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**webhook_logs** | [**List[WebhookLog]**](WebhookLog.md) |  | [optional] 
**webhook_status** | **str** |  | [optional] 

## Example

```python
from conekta.models.event_response import EventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventResponse from a JSON string
event_response_instance = EventResponse.from_json(json)
# print the JSON string representation of the object
print EventResponse.to_json()

# convert the object into a dict
event_response_dict = event_response_instance.to_dict()
# create an instance of EventResponse from a dict
event_response_form_dict = event_response.from_dict(event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


