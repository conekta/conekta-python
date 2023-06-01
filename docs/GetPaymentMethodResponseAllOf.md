# GetPaymentMethodResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetCustomerPaymentMethodDataResponse]**](GetCustomerPaymentMethodDataResponse.md) |  | [optional] 

## Example

```python
from conekta.models.get_payment_method_response_all_of import GetPaymentMethodResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentMethodResponseAllOf from a JSON string
get_payment_method_response_all_of_instance = GetPaymentMethodResponseAllOf.from_json(json)
# print the JSON string representation of the object
print GetPaymentMethodResponseAllOf.to_json()

# convert the object into a dict
get_payment_method_response_all_of_dict = get_payment_method_response_all_of_instance.to_dict()
# create an instance of GetPaymentMethodResponseAllOf from a dict
get_payment_method_response_all_of_form_dict = get_payment_method_response_all_of.from_dict(get_payment_method_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


