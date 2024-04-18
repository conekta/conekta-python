# SubscriptionEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[EventResponse]**](EventResponse.md) |  | [optional] 

## Example

```python
from conekta.models.subscription_events_response import SubscriptionEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionEventsResponse from a JSON string
subscription_events_response_instance = SubscriptionEventsResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionEventsResponse.to_json())

# convert the object into a dict
subscription_events_response_dict = subscription_events_response_instance.to_dict()
# create an instance of SubscriptionEventsResponse from a dict
subscription_events_response_from_dict = SubscriptionEventsResponse.from_dict(subscription_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


