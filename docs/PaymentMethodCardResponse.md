# PaymentMethodCardResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**object** | **str** |  | 
**created_at** | **int** |  | 
**parent_id** | **str** |  | [optional] 
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
from conekta.models.payment_method_card_response import PaymentMethodCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardResponse from a JSON string
payment_method_card_response_instance = PaymentMethodCardResponse.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCardResponse.to_json()

# convert the object into a dict
payment_method_card_response_dict = payment_method_card_response_instance.to_dict()
# create an instance of PaymentMethodCardResponse from a dict
payment_method_card_response_form_dict = payment_method_card_response.from_dict(payment_method_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


