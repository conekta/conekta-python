# TransactionResponse

The Transaction object represents the actions or steps of an order. Statuses can be: unprocessed, pending, available, owen, paid_out, voided, capture, capture_reversal, liquidation, liquidation_reversal, payout, payout_reversal, refund, refund_reversal, chargeback, chargeback_reversal, rounding_adjustment, won_chargeback, transferred, and transferred.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount of the transaction. | 
**charge** | **str** | Randomly assigned unique order identifier associated with the charge. | 
**created_at** | **int** | Date and time of creation of the transaction in Unix format. | 
**currency** | **str** | The currency of the transaction. It uses the 3-letter code of the [International Standard ISO 4217.](https://es.wikipedia.org/wiki/ISO_4217) | 
**fee** | **int** | The amount to be deducted for taxes and commissions. | 
**id** | **str** | Unique identifier of the transaction. | 
**livemode** | **bool** | Indicates whether the transaction was created in live mode or test mode. | 
**net** | **int** | The net amount after deducting commissions and taxes. | 
**object** | **str** | Object name, which is transaction. | 
**status** | **str** | Code indicating transaction status. | 
**type** | **str** | Transaction Type | 

## Example

```python
from conekta.models.transaction_response import TransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponse from a JSON string
transaction_response_instance = TransactionResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionResponse.to_json())

# convert the object into a dict
transaction_response_dict = transaction_response_instance.to_dict()
# create an instance of TransactionResponse from a dict
transaction_response_from_dict = TransactionResponse.from_dict(transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


