# ResendEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhooks_ids** | **List[str]** | webhooks ids to resend event | 

## Example

```python
from conekta.models.resend_event_request import ResendEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendEventRequest from a JSON string
resend_event_request_instance = ResendEventRequest.from_json(json)
# print the JSON string representation of the object
print(ResendEventRequest.to_json())

# convert the object into a dict
resend_event_request_dict = resend_event_request_instance.to_dict()
# create an instance of ResendEventRequest from a dict
resend_event_request_from_dict = ResendEventRequest.from_dict(resend_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


