# WebhookLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_attempts** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**last_attempted_at** | **int** |  | [optional] 
**last_http_response_status** | **int** |  | [optional] 
**object** | **str** |  | [optional] 
**response_data** | **Dict[str, object]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from conekta.models.webhook_log import WebhookLog

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLog from a JSON string
webhook_log_instance = WebhookLog.from_json(json)
# print the JSON string representation of the object
print WebhookLog.to_json()

# convert the object into a dict
webhook_log_dict = webhook_log_instance.to_dict()
# create an instance of WebhookLog from a dict
webhook_log_form_dict = webhook_log.from_dict(webhook_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


