# ChargeDataPaymentMethodBankTransferResponse

use for bank transfer responses

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank** | **str** |  | [optional] 
**clabe** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**executed_at** | **int** |  | [optional] 
**expires_at** | **int** |  | [optional] 
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
from conekta.models.charge_data_payment_method_bank_transfer_response import ChargeDataPaymentMethodBankTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeDataPaymentMethodBankTransferResponse from a JSON string
charge_data_payment_method_bank_transfer_response_instance = ChargeDataPaymentMethodBankTransferResponse.from_json(json)
# print the JSON string representation of the object
print ChargeDataPaymentMethodBankTransferResponse.to_json()

# convert the object into a dict
charge_data_payment_method_bank_transfer_response_dict = charge_data_payment_method_bank_transfer_response_instance.to_dict()
# create an instance of ChargeDataPaymentMethodBankTransferResponse from a dict
charge_data_payment_method_bank_transfer_response_form_dict = charge_data_payment_method_bank_transfer_response.from_dict(charge_data_payment_method_bank_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


