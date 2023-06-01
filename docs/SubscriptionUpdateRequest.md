# SubscriptionUpdateRequest

You can modify the subscription to change the plan used by your customers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | [optional] 
**card_id** | **str** |  | [optional] 
**trial_end** | **int** |  | [optional] 

## Example

```python
from conekta.models.subscription_update_request import SubscriptionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUpdateRequest from a JSON string
subscription_update_request_instance = SubscriptionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print SubscriptionUpdateRequest.to_json()

# convert the object into a dict
subscription_update_request_dict = subscription_update_request_instance.to_dict()
# create an instance of SubscriptionUpdateRequest from a dict
subscription_update_request_form_dict = subscription_update_request.from_dict(subscription_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


