# PaymentMethodCashResponseAllOfAgreements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement** | **str** | Agreement number, you can use this number to pay in the store/bbva | [optional] 
**provider** | **str** | Provider name, you can use this to know where to pay | [optional] 

## Example

```python
from conekta.models.payment_method_cash_response_all_of_agreements import PaymentMethodCashResponseAllOfAgreements

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCashResponseAllOfAgreements from a JSON string
payment_method_cash_response_all_of_agreements_instance = PaymentMethodCashResponseAllOfAgreements.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCashResponseAllOfAgreements.to_json())

# convert the object into a dict
payment_method_cash_response_all_of_agreements_dict = payment_method_cash_response_all_of_agreements_instance.to_dict()
# create an instance of PaymentMethodCashResponseAllOfAgreements from a dict
payment_method_cash_response_all_of_agreements_from_dict = PaymentMethodCashResponseAllOfAgreements.from_dict(payment_method_cash_response_all_of_agreements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


