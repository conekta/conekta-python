# ChargeRequestPaymentMethod

Payment method used in the charge. Go to the [payment methods](https://developers.conekta.com/reference/m%C3%A9todos-de-pago) section for more details 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **int** | Method expiration date as unix timestamp | [optional] 
**monthly_installments** | **int** | How many months without interest to apply, it can be 3, 6, 9, 12 or 18 | [optional] 
**type** | **str** |  | 
**token_id** | **str** |  | [optional] 
**payment_source_id** | **str** |  | [optional] 
**contract_id** | **str** | Optional id sent to indicate the bank contract for recurrent card charges. | [optional] 

## Example

```python
from conekta.models.charge_request_payment_method import ChargeRequestPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeRequestPaymentMethod from a JSON string
charge_request_payment_method_instance = ChargeRequestPaymentMethod.from_json(json)
# print the JSON string representation of the object
print(ChargeRequestPaymentMethod.to_json())

# convert the object into a dict
charge_request_payment_method_dict = charge_request_payment_method_instance.to_dict()
# create an instance of ChargeRequestPaymentMethod from a dict
charge_request_payment_method_from_dict = ChargeRequestPaymentMethod.from_dict(charge_request_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


