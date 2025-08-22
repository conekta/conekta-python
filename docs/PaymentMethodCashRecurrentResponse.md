# PaymentMethodCashRecurrentResponse

Alias of cash response used when type=cash_recurrent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**object** | **str** |  | 
**created_at** | **int** |  | 
**parent_id** | **str** |  | [optional] 
**agreements** | [**List[PaymentMethodCashResponseAllOfAgreements]**](PaymentMethodCashResponseAllOfAgreements.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**barcode_url** | **str** | URL to the barcode image, reference is the same as barcode | [optional] 
**expires_at** | **int** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from conekta.models.payment_method_cash_recurrent_response import PaymentMethodCashRecurrentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCashRecurrentResponse from a JSON string
payment_method_cash_recurrent_response_instance = PaymentMethodCashRecurrentResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCashRecurrentResponse.to_json())

# convert the object into a dict
payment_method_cash_recurrent_response_dict = payment_method_cash_recurrent_response_instance.to_dict()
# create an instance of PaymentMethodCashRecurrentResponse from a dict
payment_method_cash_recurrent_response_from_dict = PaymentMethodCashRecurrentResponse.from_dict(payment_method_cash_recurrent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


