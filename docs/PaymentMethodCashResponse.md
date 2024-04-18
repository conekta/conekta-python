# PaymentMethodCashResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**object** | **str** |  | 
**created_at** | **int** |  | 
**parent_id** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**barcode_url** | **str** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from conekta.models.payment_method_cash_response import PaymentMethodCashResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCashResponse from a JSON string
payment_method_cash_response_instance = PaymentMethodCashResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCashResponse.to_json())

# convert the object into a dict
payment_method_cash_response_dict = payment_method_cash_response_instance.to_dict()
# create an instance of PaymentMethodCashResponse from a dict
payment_method_cash_response_from_dict = PaymentMethodCashResponse.from_dict(payment_method_cash_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


