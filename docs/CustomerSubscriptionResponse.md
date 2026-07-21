# CustomerSubscriptionResponse

subscription model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_cycle_start** | **int** |  | [optional] 
**billing_cycle_end** | **int** |  | [optional] 
**canceled_at** | **int** |  | [optional] 
**canceled_reason** | **str** | Reason for cancellation. This field appears when the subscription status is &#39;canceled&#39;. | [optional] 
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
from conekta.models.customer_subscription_response import CustomerSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerSubscriptionResponse from a JSON string
customer_subscription_response_instance = CustomerSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerSubscriptionResponse.to_json())

# convert the object into a dict
customer_subscription_response_dict = customer_subscription_response_instance.to_dict()
# create an instance of CustomerSubscriptionResponse from a dict
customer_subscription_response_from_dict = CustomerSubscriptionResponse.from_dict(customer_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


