# PayoutOrderResponseCustomerInfo

The customer information of the payout order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_custom_reference** | **str** | Custom reference | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**corporate** | **bool** |  | [optional] [default to False]
**object** | **str** |  | [optional] 
**id** | **str** | The id of the customer. | 

## Example

```python
from conekta.models.payout_order_response_customer_info import PayoutOrderResponseCustomerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutOrderResponseCustomerInfo from a JSON string
payout_order_response_customer_info_instance = PayoutOrderResponseCustomerInfo.from_json(json)
# print the JSON string representation of the object
print(PayoutOrderResponseCustomerInfo.to_json())

# convert the object into a dict
payout_order_response_customer_info_dict = payout_order_response_customer_info_instance.to_dict()
# create an instance of PayoutOrderResponseCustomerInfo from a dict
payout_order_response_customer_info_from_dict = PayoutOrderResponseCustomerInfo.from_dict(payout_order_response_customer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


