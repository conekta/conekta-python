# ChargeDataPaymentMethodCashResponse

use for cash responses

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **int** |  | [optional] 
**cashier_id** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**barcode_url** | **str** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**service_name** | **str** |  | [optional] 
**store** | **str** |  | [optional] 
**store_name** | **str** |  | [optional] 

## Example

```python
from conekta.models.charge_data_payment_method_cash_response import ChargeDataPaymentMethodCashResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeDataPaymentMethodCashResponse from a JSON string
charge_data_payment_method_cash_response_instance = ChargeDataPaymentMethodCashResponse.from_json(json)
# print the JSON string representation of the object
print ChargeDataPaymentMethodCashResponse.to_json()

# convert the object into a dict
charge_data_payment_method_cash_response_dict = charge_data_payment_method_cash_response_instance.to_dict()
# create an instance of ChargeDataPaymentMethodCashResponse from a dict
charge_data_payment_method_cash_response_form_dict = charge_data_payment_method_cash_response.from_dict(charge_data_payment_method_cash_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


