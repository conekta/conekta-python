# PaymentMethodPbbRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the payment method | 
**expires_at** | **int** | Expiration date of the payment method, in Unix timestamp format | [optional] 
**product_type** | **str** | Product type of the payment method, use for the payment method to know the product type | 

## Example

```python
from conekta.models.payment_method_pbb_request import PaymentMethodPbbRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodPbbRequest from a JSON string
payment_method_pbb_request_instance = PaymentMethodPbbRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodPbbRequest.to_json())

# convert the object into a dict
payment_method_pbb_request_dict = payment_method_pbb_request_instance.to_dict()
# create an instance of PaymentMethodPbbRequest from a dict
payment_method_pbb_request_from_dict = PaymentMethodPbbRequest.from_dict(payment_method_pbb_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


