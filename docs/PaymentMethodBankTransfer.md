# PaymentMethodBankTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**object** | **str** |  | 
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
from conekta.models.payment_method_bank_transfer import PaymentMethodBankTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBankTransfer from a JSON string
payment_method_bank_transfer_instance = PaymentMethodBankTransfer.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodBankTransfer.to_json())

# convert the object into a dict
payment_method_bank_transfer_dict = payment_method_bank_transfer_instance.to_dict()
# create an instance of PaymentMethodBankTransfer from a dict
payment_method_bank_transfer_from_dict = PaymentMethodBankTransfer.from_dict(payment_method_bank_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


