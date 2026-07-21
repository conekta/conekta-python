# PayoutOrderRequestCustomerInfo

The customer information to whom the payout order is made.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | 

## Example

```python
from conekta.models.payout_order_request_customer_info import PayoutOrderRequestCustomerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutOrderRequestCustomerInfo from a JSON string
payout_order_request_customer_info_instance = PayoutOrderRequestCustomerInfo.from_json(json)
# print the JSON string representation of the object
print(PayoutOrderRequestCustomerInfo.to_json())

# convert the object into a dict
payout_order_request_customer_info_dict = payout_order_request_customer_info_instance.to_dict()
# create an instance of PayoutOrderRequestCustomerInfo from a dict
payout_order_request_customer_info_from_dict = PayoutOrderRequestCustomerInfo.from_dict(payout_order_request_customer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


