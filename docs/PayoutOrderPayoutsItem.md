# PayoutOrderPayoutsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount of the payout. | 
**currency** | **str** | The currency in which the payout is made. | 
**expires_at** | **int** | The expiration date of the payout. | [optional] 
**id** | **str** | The id of the payout. | 
**livemode** | **bool** | The live mode of the payout. | 
**object** | **str** | The object of the payout. | 
**payout_order_id** | **str** | The id of the payout order. | [optional] 
**status** | **str** | The status of the payout. | [optional] 

## Example

```python
from conekta.models.payout_order_payouts_item import PayoutOrderPayoutsItem

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutOrderPayoutsItem from a JSON string
payout_order_payouts_item_instance = PayoutOrderPayoutsItem.from_json(json)
# print the JSON string representation of the object
print(PayoutOrderPayoutsItem.to_json())

# convert the object into a dict
payout_order_payouts_item_dict = payout_order_payouts_item_instance.to_dict()
# create an instance of PayoutOrderPayoutsItem from a dict
payout_order_payouts_item_from_dict = PayoutOrderPayoutsItem.from_dict(payout_order_payouts_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


