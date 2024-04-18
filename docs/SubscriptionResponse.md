# SubscriptionResponse

subscription model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_cycle_start** | **int** |  | [optional] 
**billing_cycle_end** | **int** |  | [optional] 
**canceled_at** | **int** |  | [optional] 
**card_id** | **str** |  | [optional] 
**charge_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**customer_custom_reference** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_billing_cycle_order_id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**paused_at** | **int** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**subscription_start** | **int** |  | [optional] 
**trial_start** | **int** |  | [optional] 
**trial_end** | **int** |  | [optional] 

## Example

```python
from conekta.models.subscription_response import SubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponse from a JSON string
subscription_response_instance = SubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponse.to_json())

# convert the object into a dict
subscription_response_dict = subscription_response_instance.to_dict()
# create an instance of SubscriptionResponse from a dict
subscription_response_from_dict = SubscriptionResponse.from_dict(subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


