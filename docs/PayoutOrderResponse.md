# PayoutOrderResponse

payout order model response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_payout_methods** | **List[str]** | The payout methods that are allowed for the payout order. | 
**amount** | **int** | The amount of the payout order. | 
**created_at** | **int** | The creation date of the payout order. | 
**currency** | **str** | The currency in which the payout order is made. | [default to 'MXN']
**customer_info** | [**PayoutOrderResponseCustomerInfo**](PayoutOrderResponseCustomerInfo.md) |  | 
**expires_at** | **int** | The expiration date of the payout order. | [optional] 
**id** | **str** | The id of the payout order. | 
**livemode** | **bool** | The live mode of the payout order. | 
**object** | **str** | The object of the payout order. | 
**metadata** | **Dict[str, object]** | The metadata of the payout order. | [optional] 
**payouts** | [**List[PayoutOrderPayoutsItem]**](PayoutOrderPayoutsItem.md) | The payout information of the payout order. | 
**reason** | **str** | The reason for the payout order. | 
**status** | **str** | The status of the payout order. | [optional] 
**updated_at** | **int** | The update date of the payout order. | 

## Example

```python
from conekta.models.payout_order_response import PayoutOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutOrderResponse from a JSON string
payout_order_response_instance = PayoutOrderResponse.from_json(json)
# print the JSON string representation of the object
print(PayoutOrderResponse.to_json())

# convert the object into a dict
payout_order_response_dict = payout_order_response_instance.to_dict()
# create an instance of PayoutOrderResponse from a dict
payout_order_response_from_dict = PayoutOrderResponse.from_dict(payout_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


