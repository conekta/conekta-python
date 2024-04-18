# PaymentMethodCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**object** | **str** |  | 
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
from conekta.models.payment_method_card import PaymentMethodCard

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCard from a JSON string
payment_method_card_instance = PaymentMethodCard.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCard.to_json())

# convert the object into a dict
payment_method_card_dict = payment_method_card_instance.to_dict()
# create an instance of PaymentMethodCard from a dict
payment_method_card_from_dict = PaymentMethodCard.from_dict(payment_method_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


