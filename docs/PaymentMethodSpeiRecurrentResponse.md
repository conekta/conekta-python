# PaymentMethodSpeiRecurrentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**object** | **str** |  | 
**created_at** | **int** |  | 
**parent_id** | **str** |  | [optional] 
**bank** | **str** | Bank name for the SPEI payment method | [optional] 
**reference** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 

## Example

```python
from conekta.models.payment_method_spei_recurrent_response import PaymentMethodSpeiRecurrentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodSpeiRecurrentResponse from a JSON string
payment_method_spei_recurrent_response_instance = PaymentMethodSpeiRecurrentResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodSpeiRecurrentResponse.to_json())

# convert the object into a dict
payment_method_spei_recurrent_response_dict = payment_method_spei_recurrent_response_instance.to_dict()
# create an instance of PaymentMethodSpeiRecurrentResponse from a dict
payment_method_spei_recurrent_response_from_dict = PaymentMethodSpeiRecurrentResponse.from_dict(payment_method_spei_recurrent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


