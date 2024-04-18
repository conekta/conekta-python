# WebhookResponse

webhooks model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** |  | [optional] 
**development_enabled** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**livemode** | **bool** |  | [optional] 
**object** | **str** |  | [optional] 
**production_enabled** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**subscribed_events** | **List[str]** |  | [optional] 
**synchronous** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from conekta.models.webhook_response import WebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookResponse from a JSON string
webhook_response_instance = WebhookResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookResponse.to_json())

# convert the object into a dict
webhook_response_dict = webhook_response_instance.to_dict()
# create an instance of WebhookResponse from a dict
webhook_response_from_dict = WebhookResponse.from_dict(webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


