# PaymentMethodCardResponseAllOf

use for card responses

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last4** | **str** |  | [optional] 
**bin** | **str** |  | [optional] 
**card_type** | **str** |  | [optional] 
**exp_month** | **str** |  | [optional] 
**exp_year** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**visible_on_checkout** | **bool** |  | [optional] 
**payment_source_status** | **str** |  | [optional] 

## Example

```python
from conekta.models.payment_method_card_response_all_of import PaymentMethodCardResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardResponseAllOf from a JSON string
payment_method_card_response_all_of_instance = PaymentMethodCardResponseAllOf.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCardResponseAllOf.to_json()

# convert the object into a dict
payment_method_card_response_all_of_dict = payment_method_card_response_all_of_instance.to_dict()
# create an instance of PaymentMethodCardResponseAllOf from a dict
payment_method_card_response_all_of_form_dict = payment_method_card_response_all_of.from_dict(payment_method_card_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


