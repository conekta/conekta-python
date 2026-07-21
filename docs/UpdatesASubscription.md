# UpdatesASubscription

You can modify the subscription to change the plan used by your customers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | [optional] 
**card_id** | **str** |  | [optional] 
**trial_end** | **int** |  | [optional] 

## Example

```python
from conekta.models.updates_a_subscription import UpdatesASubscription

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatesASubscription from a JSON string
updates_a_subscription_instance = UpdatesASubscription.from_json(json)
# print the JSON string representation of the object
print(UpdatesASubscription.to_json())

# convert the object into a dict
updates_a_subscription_dict = updates_a_subscription_instance.to_dict()
# create an instance of UpdatesASubscription from a dict
updates_a_subscription_from_dict = UpdatesASubscription.from_dict(updates_a_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


