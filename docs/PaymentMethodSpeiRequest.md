# PaymentMethodSpeiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of payment method | 
**expires_at** | **int** |  | [optional] 

## Example

```python
from conekta.models.payment_method_spei_request import PaymentMethodSpeiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodSpeiRequest from a JSON string
payment_method_spei_request_instance = PaymentMethodSpeiRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodSpeiRequest.to_json())

# convert the object into a dict
payment_method_spei_request_dict = payment_method_spei_request_instance.to_dict()
# create an instance of PaymentMethodSpeiRequest from a dict
payment_method_spei_request_from_dict = PaymentMethodSpeiRequest.from_dict(payment_method_spei_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


