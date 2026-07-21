# PayoutOrderRequest

a payout order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_payout_methods** | **List[str]** | The payout methods that are allowed for the payout order. | 
**amount** | **int** | The amount of the payout order. | 
**currency** | **str** | The currency in which the payout order is made. | [default to 'MXN']
**customer_info** | [**PayoutOrderRequestCustomerInfo**](PayoutOrderRequestCustomerInfo.md) |  | 
**expires_at** | **int** | The expiration time of the payout order in Unix timestamp. | 
**metadata** | **Dict[str, object]** | The metadata of the payout order. | [optional] 
**payout** | [**Payout**](Payout.md) |  | 
**reason** | **str** | The reason for the payout order. | 

## Example

```python
from conekta.models.payout_order_request import PayoutOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutOrderRequest from a JSON string
payout_order_request_instance = PayoutOrderRequest.from_json(json)
# print the JSON string representation of the object
print(PayoutOrderRequest.to_json())

# convert the object into a dict
payout_order_request_dict = payout_order_request_instance.to_dict()
# create an instance of PayoutOrderRequest from a dict
payout_order_request_from_dict = PayoutOrderRequest.from_dict(payout_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


