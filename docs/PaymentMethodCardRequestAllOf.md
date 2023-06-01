# PaymentMethodCardRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | Token id that will be used to create a \&quot;card\&quot; type payment method. See the (subscriptions)[https://developers.conekta.com/v2.1.0/reference/createsubscription] tutorial for more information on how to tokenize cards. | [optional] 

## Example

```python
from conekta.models.payment_method_card_request_all_of import PaymentMethodCardRequestAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardRequestAllOf from a JSON string
payment_method_card_request_all_of_instance = PaymentMethodCardRequestAllOf.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCardRequestAllOf.to_json()

# convert the object into a dict
payment_method_card_request_all_of_dict = payment_method_card_request_all_of_instance.to_dict()
# create an instance of PaymentMethodCardRequestAllOf from a dict
payment_method_card_request_all_of_form_dict = payment_method_card_request_all_of.from_dict(payment_method_card_request_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


