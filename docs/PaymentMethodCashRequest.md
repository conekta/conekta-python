# PaymentMethodCashRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of payment method | 
**expires_at** | **int** |  | [optional] 

## Example

```python
from conekta.models.payment_method_cash_request import PaymentMethodCashRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCashRequest from a JSON string
payment_method_cash_request_instance = PaymentMethodCashRequest.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCashRequest.to_json()

# convert the object into a dict
payment_method_cash_request_dict = payment_method_cash_request_instance.to_dict()
# create an instance of PaymentMethodCashRequest from a dict
payment_method_cash_request_form_dict = payment_method_cash_request.from_dict(payment_method_cash_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


