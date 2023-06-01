# PaymentMethodCashResponseAllOf

use for cash responses

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**barcode_url** | **str** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from conekta.models.payment_method_cash_response_all_of import PaymentMethodCashResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCashResponseAllOf from a JSON string
payment_method_cash_response_all_of_instance = PaymentMethodCashResponseAllOf.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCashResponseAllOf.to_json()

# convert the object into a dict
payment_method_cash_response_all_of_dict = payment_method_cash_response_all_of_instance.to_dict()
# create an instance of PaymentMethodCashResponseAllOf from a dict
payment_method_cash_response_all_of_form_dict = payment_method_cash_response_all_of.from_dict(payment_method_cash_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


