# GetWebhooksResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WebhookResponse]**](WebhookResponse.md) |  | [optional] 

## Example

```python
from conekta.models.get_webhooks_response_all_of import GetWebhooksResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhooksResponseAllOf from a JSON string
get_webhooks_response_all_of_instance = GetWebhooksResponseAllOf.from_json(json)
# print the JSON string representation of the object
print GetWebhooksResponseAllOf.to_json()

# convert the object into a dict
get_webhooks_response_all_of_dict = get_webhooks_response_all_of_instance.to_dict()
# create an instance of GetWebhooksResponseAllOf from a dict
get_webhooks_response_all_of_form_dict = get_webhooks_response_all_of.from_dict(get_webhooks_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


