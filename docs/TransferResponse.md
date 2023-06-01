# TransferResponse

A transfer represents the action of sending an amount to a business bank account including the status, amount and method used to make the transfer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Amount in cents of the transfer. | [optional] 
**created_at** | **int** | Date and time of creation of the transfer in Unix format. | [optional] 
**currency** | **str** | The currency of the transfer. It uses the 3-letter code of the [International Standard ISO 4217.](https://es.wikipedia.org/wiki/ISO_4217) | [optional] 
**id** | **str** | Unique identifier of the transfer. | [optional] 
**livemode** | **bool** | Indicates whether the transfer was created in live mode or test mode. | [optional] 
**destination** | [**TransferDestinationResponse**](TransferDestinationResponse.md) |  | [optional] 
**object** | **str** | Object name, which is transfer. | [optional] 
**statement_description** | **str** | Description of the transfer. | [optional] 
**statement_reference** | **str** | Reference number of the transfer. | [optional] 
**status** | **str** | Code indicating transfer status. | [optional] 

## Example

```python
from conekta.models.transfer_response import TransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransferResponse from a JSON string
transfer_response_instance = TransferResponse.from_json(json)
# print the JSON string representation of the object
print TransferResponse.to_json()

# convert the object into a dict
transfer_response_dict = transfer_response_instance.to_dict()
# create an instance of TransferResponse from a dict
transfer_response_form_dict = transfer_response.from_dict(transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


