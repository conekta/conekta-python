# GetWebhookKeysResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[WebhookKeyResponse]**](WebhookKeyResponse.md) |  | [optional] 

## Example

```python
from conekta.models.get_webhook_keys_response import GetWebhookKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhookKeysResponse from a JSON string
get_webhook_keys_response_instance = GetWebhookKeysResponse.from_json(json)
# print the JSON string representation of the object
print GetWebhookKeysResponse.to_json()

# convert the object into a dict
get_webhook_keys_response_dict = get_webhook_keys_response_instance.to_dict()
# create an instance of GetWebhookKeysResponse from a dict
get_webhook_keys_response_form_dict = get_webhook_keys_response.from_dict(get_webhook_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


