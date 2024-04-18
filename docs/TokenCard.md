# TokenCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvc** | **str** | It is a value that allows identifying the security code of the card. | 
**device_fingerprint** | **str** | It is a value that allows identifying the device fingerprint. | [optional] 
**exp_month** | **str** | It is a value that allows identifying the expiration month of the card. | 
**exp_year** | **str** | It is a value that allows identifying the expiration year of the card. | 
**name** | **str** | It is a value that allows identifying the name of the cardholder. | 
**number** | **str** | It is a value that allows identifying the number of the card. | 

## Example

```python
from conekta.models.token_card import TokenCard

# TODO update the JSON string below
json = "{}"
# create an instance of TokenCard from a JSON string
token_card_instance = TokenCard.from_json(json)
# print the JSON string representation of the object
print(TokenCard.to_json())

# convert the object into a dict
token_card_dict = token_card_instance.to_dict()
# create an instance of TokenCard from a dict
token_card_from_dict = TokenCard.from_dict(token_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


