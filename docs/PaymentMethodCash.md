# PaymentMethodCash


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**object** | **str** |  | 
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
from conekta.models.payment_method_cash import PaymentMethodCash

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCash from a JSON string
payment_method_cash_instance = PaymentMethodCash.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCash.to_json()

# convert the object into a dict
payment_method_cash_dict = payment_method_cash_instance.to_dict()
# create an instance of PaymentMethodCash from a dict
payment_method_cash_form_dict = payment_method_cash.from_dict(payment_method_cash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


