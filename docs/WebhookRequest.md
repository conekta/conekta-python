# WebhookRequest

a webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Here you must place the URL of your Webhook remember that you must program what you will do with the events received. Also do not forget to handle the HTTPS protocol for greater security. | 
**synchronous** | **bool** | It is a value that allows to decide if the events will be synchronous or asynchronous. We recommend asynchronous &#x3D; false | [default to False]

## Example

```python
from conekta.models.webhook_request import WebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRequest from a JSON string
webhook_request_instance = WebhookRequest.from_json(json)
# print the JSON string representation of the object
print WebhookRequest.to_json()

# convert the object into a dict
webhook_request_dict = webhook_request_instance.to_dict()
# create an instance of WebhookRequest from a dict
webhook_request_form_dict = webhook_request.from_dict(webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


