# PaymentMethodTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of payment method | 
**token_id** | **str** | Token id that will be used to create a \&quot;card\&quot; type payment method. See the (subscriptions)[https://developers.conekta.com/v2.2.0/reference/createsubscription] tutorial for more information on how to tokenize cards. | 

## Example

```python
from conekta.models.payment_method_token_request import PaymentMethodTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodTokenRequest from a JSON string
payment_method_token_request_instance = PaymentMethodTokenRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodTokenRequest.to_json())

# convert the object into a dict
payment_method_token_request_dict = payment_method_token_request_instance.to_dict()
# create an instance of PaymentMethodTokenRequest from a dict
payment_method_token_request_from_dict = PaymentMethodTokenRequest.from_dict(payment_method_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


