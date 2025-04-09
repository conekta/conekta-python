# WebhookResponse

webhooks model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the webhook | [optional] 
**description** | **str** | A name or brief explanation of what this webhook is used for | [optional] 
**livemode** | **bool** | Indicates if the webhook is in production | [optional] 
**active** | **bool** | Indicates if the webhook is actived or not | [optional] 
**object** | **str** | Object name, value is &#39;webhook&#39; | [optional] 
**status** | **str** | Indicates if the webhook is ready to receive events or failing | [optional] 
**subscribed_events** | **List[str]** | lists the events that will be sent to the webhook | [optional] 
**url** | **str** | url or endpoint of the webhook | [optional] 

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


