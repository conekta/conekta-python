# GetWebhookKeysResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WebhookKeyResponse]**](WebhookKeyResponse.md) |  | [optional] 

## Example

```python
from conekta.models.get_webhook_keys_response_all_of import GetWebhookKeysResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhookKeysResponseAllOf from a JSON string
get_webhook_keys_response_all_of_instance = GetWebhookKeysResponseAllOf.from_json(json)
# print the JSON string representation of the object
print GetWebhookKeysResponseAllOf.to_json()

# convert the object into a dict
get_webhook_keys_response_all_of_dict = get_webhook_keys_response_all_of_instance.to_dict()
# create an instance of GetWebhookKeysResponseAllOf from a dict
get_webhook_keys_response_all_of_form_dict = get_webhook_keys_response_all_of.from_dict(get_webhook_keys_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


