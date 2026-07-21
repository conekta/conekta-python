# SubscriptionDetails

Subscription details for customer portal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**SubscriptionDetailsCard**](SubscriptionDetailsCard.md) |  | [optional] 
**plan** | [**SubscriptionDetailsPlan**](SubscriptionDetailsPlan.md) |  | [optional] 
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**next_billing_cycle** | **int** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 

## Example

```python
from conekta.models.subscription_details import SubscriptionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDetails from a JSON string
subscription_details_instance = SubscriptionDetails.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDetails.to_json())

# convert the object into a dict
subscription_details_dict = subscription_details_instance.to_dict()
# create an instance of SubscriptionDetails from a dict
subscription_details_from_dict = SubscriptionDetails.from_dict(subscription_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


