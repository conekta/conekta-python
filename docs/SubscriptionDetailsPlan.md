# SubscriptionDetailsPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**amount** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**interval** | **str** |  | [optional] 
**frequency** | **int** |  | [optional] 
**trial_period_days** | **int** |  | [optional] 
**expiry_count** | **int** |  | [optional] 
**created_at** | **int** |  | [optional] 

## Example

```python
from conekta.models.subscription_details_plan import SubscriptionDetailsPlan

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDetailsPlan from a JSON string
subscription_details_plan_instance = SubscriptionDetailsPlan.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDetailsPlan.to_json())

# convert the object into a dict
subscription_details_plan_dict = subscription_details_plan_instance.to_dict()
# create an instance of SubscriptionDetailsPlan from a dict
subscription_details_plan_from_dict = SubscriptionDetailsPlan.from_dict(subscription_details_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


