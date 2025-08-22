# PaymentMethodPbbPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**object** | **str** |  | 
**deep_link** | **str** | Deep link for the payment, use for mobile apps/flows | 
**expires_at** | **int** | Expiration date of the charge | 
**product_type** | **str** | Product type of the charge | 
**redirect_url** | **str** | URL to redirect the customer to complete the payment | 
**reference** | **str** | Reference for the payment | 

## Example

```python
from conekta.models.payment_method_pbb_payment import PaymentMethodPbbPayment

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodPbbPayment from a JSON string
payment_method_pbb_payment_instance = PaymentMethodPbbPayment.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodPbbPayment.to_json())

# convert the object into a dict
payment_method_pbb_payment_dict = payment_method_pbb_payment_instance.to_dict()
# create an instance of PaymentMethodPbbPayment from a dict
payment_method_pbb_payment_from_dict = PaymentMethodPbbPayment.from_dict(payment_method_pbb_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


