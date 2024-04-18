# PaymentMethodSpeiRecurrent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**object** | **str** |  | 
**created_at** | **int** |  | 
**parent_id** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 

## Example

```python
from conekta.models.payment_method_spei_recurrent import PaymentMethodSpeiRecurrent

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodSpeiRecurrent from a JSON string
payment_method_spei_recurrent_instance = PaymentMethodSpeiRecurrent.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodSpeiRecurrent.to_json())

# convert the object into a dict
payment_method_spei_recurrent_dict = payment_method_spei_recurrent_instance.to_dict()
# create an instance of PaymentMethodSpeiRecurrent from a dict
payment_method_spei_recurrent_from_dict = PaymentMethodSpeiRecurrent.from_dict(payment_method_spei_recurrent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


