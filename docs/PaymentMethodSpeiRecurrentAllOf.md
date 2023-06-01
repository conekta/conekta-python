# PaymentMethodSpeiRecurrentAllOf

use for spei responses

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 

## Example

```python
from conekta.models.payment_method_spei_recurrent_all_of import PaymentMethodSpeiRecurrentAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodSpeiRecurrentAllOf from a JSON string
payment_method_spei_recurrent_all_of_instance = PaymentMethodSpeiRecurrentAllOf.from_json(json)
# print the JSON string representation of the object
print PaymentMethodSpeiRecurrentAllOf.to_json()

# convert the object into a dict
payment_method_spei_recurrent_all_of_dict = payment_method_spei_recurrent_all_of_instance.to_dict()
# create an instance of PaymentMethodSpeiRecurrentAllOf from a dict
payment_method_spei_recurrent_all_of_form_dict = payment_method_spei_recurrent_all_of.from_dict(payment_method_spei_recurrent_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


