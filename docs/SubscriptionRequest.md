# SubscriptionRequest

It is a parameter that allows to identify in the response, the detailed content of the plans to which the client has subscribed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | 
**card_id** | **str** |  | [optional] 
**trial_end** | **int** |  | [optional] 

## Example

```python
from conekta.models.subscription_request import SubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionRequest from a JSON string
subscription_request_instance = SubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionRequest.to_json())

# convert the object into a dict
subscription_request_dict = subscription_request_instance.to_dict()
# create an instance of SubscriptionRequest from a dict
subscription_request_from_dict = SubscriptionRequest.from_dict(subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


