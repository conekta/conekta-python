# PaymentMethodCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**object** | **str** |  | 
**account_type** | **str** | Account type of the card | [optional] 
**auth_code** | **str** |  | [optional] 
**brand** | **str** | Brand of the card | [optional] 
**contract_id** | **str** | Id sent for recurrent charges. | [optional] 
**country** | **str** | Country of the card | [optional] 
**exp_month** | **str** | Expiration month of the card | [optional] 
**exp_year** | **str** | Expiration year of the card | [optional] 
**fraud_indicators** | **List[object]** |  | [optional] 
**issuer** | **str** | Issuer of the card | [optional] 
**last4** | **str** | Last 4 digits of the card | [optional] 
**name** | **str** | Name of the cardholder | [optional] 
**customer_ip_address** | **str** | Optional field used to capture the customer&#39;s IP address for fraud prevention and security monitoring purposes | [optional] 

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


