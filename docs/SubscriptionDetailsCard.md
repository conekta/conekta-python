# SubscriptionDetailsCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**active** | **bool** |  | [optional] 
**object** | **str** |  | [optional] 
**exp_month** | **str** |  | [optional] 
**exp_year** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**last4** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**payment_source_status** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**customer_custom_reference** | **str** |  | [optional] 

## Example

```python
from conekta.models.subscription_details_card import SubscriptionDetailsCard

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDetailsCard from a JSON string
subscription_details_card_instance = SubscriptionDetailsCard.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDetailsCard.to_json())

# convert the object into a dict
subscription_details_card_dict = subscription_details_card_instance.to_dict()
# create an instance of SubscriptionDetailsCard from a dict
subscription_details_card_from_dict = SubscriptionDetailsCard.from_dict(subscription_details_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


