# PaymentMethodBnplPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**object** | **str** |  | 
**cancel_url** | **str** | URL to redirect the customer after a canceled payment | [optional] 
**expires_at** | **int** | Expiration date of the charge | 
**failure_url** | **str** | URL to redirect the customer after a failed payment | [optional] 
**product_type** | **str** | Product type of the charge | 
**redirect_url** | **str** | URL to redirect the customer to complete the payment | [optional] 
**success_url** | **str** | URL to redirect the customer after a successful payment | [optional] 

## Example

```python
from conekta.models.payment_method_bnpl_payment import PaymentMethodBnplPayment

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBnplPayment from a JSON string
payment_method_bnpl_payment_instance = PaymentMethodBnplPayment.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodBnplPayment.to_json())

# convert the object into a dict
payment_method_bnpl_payment_dict = payment_method_bnpl_payment_instance.to_dict()
# create an instance of PaymentMethodBnplPayment from a dict
payment_method_bnpl_payment_from_dict = PaymentMethodBnplPayment.from_dict(payment_method_bnpl_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


