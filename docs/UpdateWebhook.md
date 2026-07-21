# UpdateWebhook

an updated webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Here you must place the URL of your Webhook remember that you must program what you will do with the events received. Also do not forget to handle the HTTPS protocol for greater security. | [optional] 
**subscribed_events** | **List[str]** | events that will be sent to the webhook | [optional] 
**active** | **bool** | whether the webhook is active or not | [optional] 

## Example

```python
from conekta.models.update_webhook import UpdateWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhook from a JSON string
update_webhook_instance = UpdateWebhook.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhook.to_json())

# convert the object into a dict
update_webhook_dict = update_webhook_instance.to_dict()
# create an instance of UpdateWebhook from a dict
update_webhook_from_dict = UpdateWebhook.from_dict(update_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


