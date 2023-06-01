# WebhookKeyResponse

webhook keys model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the webhook key | [optional] 
**active** | **bool** | Indicates if the webhook key is active | [optional] 
**created_at** | **int** | Unix timestamp in seconds with the creation date of the webhook key | [optional] 
**deactivated_at** | **int** | Unix timestamp in seconds with the deactivation date of the webhook key | [optional] 
**public_key** | **str** | Public key to be used in the webhook | [optional] 
**livemode** | **bool** | Indicates if the webhook key is in live mode | [optional] 
**object** | **str** | Object name, value is webhook_key | [optional] 

## Example

```python
from conekta.models.webhook_key_response import WebhookKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookKeyResponse from a JSON string
webhook_key_response_instance = WebhookKeyResponse.from_json(json)
# print the JSON string representation of the object
print WebhookKeyResponse.to_json()

# convert the object into a dict
webhook_key_response_dict = webhook_key_response_instance.to_dict()
# create an instance of WebhookKeyResponse from a dict
webhook_key_response_form_dict = webhook_key_response.from_dict(webhook_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


