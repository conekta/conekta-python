# TransferMethodResponse

Method used to make the transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | **str** | Name of the account holder. | [optional] 
**account_number** | **str** | Account number of the bank account. | [optional] 
**bank** | **str** | Name of the bank. | [optional] 
**created_at** | **int** | Date and time of creation of the transfer. | [optional] 
**id** | **str** | Unique identifier of the transfer. | [optional] 
**object** | **str** | Object name, which is bank_transfer_payout_method. | [optional] 
**payee_id** | **str** | Unique identifier of the payee. | [optional] 
**type** | **str** | Type of the payee. | [optional] 

## Example

```python
from conekta.models.transfer_method_response import TransferMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransferMethodResponse from a JSON string
transfer_method_response_instance = TransferMethodResponse.from_json(json)
# print the JSON string representation of the object
print(TransferMethodResponse.to_json())

# convert the object into a dict
transfer_method_response_dict = transfer_method_response_instance.to_dict()
# create an instance of TransferMethodResponse from a dict
transfer_method_response_from_dict = TransferMethodResponse.from_dict(transfer_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


