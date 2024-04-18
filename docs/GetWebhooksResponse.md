# GetWebhooksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[WebhookResponse]**](WebhookResponse.md) |  | [optional] 

## Example

```python
from conekta.models.get_webhooks_response import GetWebhooksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhooksResponse from a JSON string
get_webhooks_response_instance = GetWebhooksResponse.from_json(json)
# print the JSON string representation of the object
print(GetWebhooksResponse.to_json())

# convert the object into a dict
get_webhooks_response_dict = get_webhooks_response_instance.to_dict()
# create an instance of GetWebhooksResponse from a dict
get_webhooks_response_from_dict = GetWebhooksResponse.from_dict(get_webhooks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


