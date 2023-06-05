# ChargeResponsePaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**object** | **str** |  | 
**auth_code** | **str** |  | [optional] 
**cashier_id** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**barcode_url** | **str** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**service_name** | **str** |  | [optional] 
**store** | **str** |  | [optional] 
**store_name** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**exp_month** | **str** |  | [optional] 
**exp_year** | **str** |  | [optional] 
**fraud_indicators** | **List[object]** |  | [optional] 
**issuer** | **str** |  | [optional] 
**last4** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**bank** | **str** |  | [optional] 
**clabe** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**executed_at** | **int** |  | [optional] 
**issuing_account_bank** | **str** |  | [optional] 
**issuing_account_number** | **str** |  | [optional] 
**issuing_account_holder_name** | **str** |  | [optional] 
**issuing_account_tax_id** | **str** |  | [optional] 
**payment_attempts** | **List[object]** |  | [optional] 
**receiving_account_holder_name** | **str** |  | [optional] 
**receiving_account_number** | **str** |  | [optional] 
**receiving_account_bank** | **str** |  | [optional] 
**receiving_account_tax_id** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**tracking_code** | **str** |  | [optional] 

## Example

```python
from conekta.models.charge_response_payment_method import ChargeResponsePaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeResponsePaymentMethod from a JSON string
charge_response_payment_method_instance = ChargeResponsePaymentMethod.from_json(json)
# print the JSON string representation of the object
print ChargeResponsePaymentMethod.to_json()

# convert the object into a dict
charge_response_payment_method_dict = charge_response_payment_method_instance.to_dict()
# create an instance of ChargeResponsePaymentMethod from a dict
charge_response_payment_method_form_dict = charge_response_payment_method.from_dict(charge_response_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


