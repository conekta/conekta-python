# WebhookKeyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if the webhook key is active | [optional] [default to True]

## Example

```python
from conekta.models.webhook_key_request import WebhookKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookKeyRequest from a JSON string
webhook_key_request_instance = WebhookKeyRequest.from_json(json)
# print the JSON string representation of the object
print WebhookKeyRequest.to_json()

# convert the object into a dict
webhook_key_request_dict = webhook_key_request_instance.to_dict()
# create an instance of WebhookKeyRequest from a dict
webhook_key_request_form_dict = webhook_key_request.from_dict(webhook_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


