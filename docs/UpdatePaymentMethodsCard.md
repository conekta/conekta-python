# UpdatePaymentMethodsCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the payment method holder | [optional] 
**expires_at** | **int** | The expiration date of the payment method in Unix timestamp format | [optional] 

## Example

```python
from conekta.models.update_payment_methods_card import UpdatePaymentMethodsCard

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaymentMethodsCard from a JSON string
update_payment_methods_card_instance = UpdatePaymentMethodsCard.from_json(json)
# print the JSON string representation of the object
print(UpdatePaymentMethodsCard.to_json())

# convert the object into a dict
update_payment_methods_card_dict = update_payment_methods_card_instance.to_dict()
# create an instance of UpdatePaymentMethodsCard from a dict
update_payment_methods_card_from_dict = UpdatePaymentMethodsCard.from_dict(update_payment_methods_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


