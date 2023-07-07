# ChargeDataPaymentMethodCardResponse

use for card responses

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** |  | [optional] 
**auth_code** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**contract_id** | **str** | Id sent for recurrent charges. | [optional] 
**country** | **str** |  | [optional] 
**exp_month** | **str** |  | [optional] 
**exp_year** | **str** |  | [optional] 
**fraud_indicators** | **List[object]** |  | [optional] 
**issuer** | **str** |  | [optional] 
**last4** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from conekta.models.charge_data_payment_method_card_response import ChargeDataPaymentMethodCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeDataPaymentMethodCardResponse from a JSON string
charge_data_payment_method_card_response_instance = ChargeDataPaymentMethodCardResponse.from_json(json)
# print the JSON string representation of the object
print ChargeDataPaymentMethodCardResponse.to_json()

# convert the object into a dict
charge_data_payment_method_card_response_dict = charge_data_payment_method_card_response_instance.to_dict()
# create an instance of ChargeDataPaymentMethodCardResponse from a dict
charge_data_payment_method_card_response_form_dict = charge_data_payment_method_card_response.from_dict(charge_data_payment_method_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


